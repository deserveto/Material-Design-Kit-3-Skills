#!/usr/bin/env node

const DISCLAIMER = "Rendered review aid only; results are not Material Design, WCAG, or accessibility certification.";

function usage() {
  return `Usage:
  node audit_runtime.mjs --base-url <url> [--paths /,/settings] [--viewports 360x800,1440x900] [--json] [--strict]

Options:
  --base-url <url>       Running application origin, for example http://localhost:3000
  --paths <list>         Comma-separated paths to inspect (default: /)
  --viewports <list>     Comma-separated WIDTHxHEIGHT viewports (default: 360x800,1440x900)
  --json                 Emit machine-readable JSON
  --strict               Exit 1 when rendered findings are detected
  --help                 Show this help without loading optional dependencies

Optional dependencies for a real audit:
  npm install --save-dev playwright @axe-core/playwright
`;
}

function parseArgs(argv) {
  const args = {baseUrl: null, paths: ["/"], viewports: [{width: 360, height: 800}, {width: 1440, height: 900}], json: false, strict: false, help: false};
  for (let i = 0; i < argv.length; i += 1) {
    const value = argv[i];
    if (value === "--help" || value === "-h") args.help = true;
    else if (value === "--json") args.json = true;
    else if (value === "--strict") args.strict = true;
    else if (value === "--base-url") args.baseUrl = argv[++i] ?? null;
    else if (value === "--paths") args.paths = (argv[++i] ?? "").split(",").map((x) => x.trim()).filter(Boolean);
    else if (value === "--viewports") {
      args.viewports = (argv[++i] ?? "").split(",").filter(Boolean).map((item) => {
        const match = /^(\d+)x(\d+)$/i.exec(item.trim());
        if (!match) throw new Error(`Invalid viewport: ${item}`);
        return {width: Number(match[1]), height: Number(match[2])};
      });
    } else throw new Error(`Unknown argument: ${value}`);
  }
  if (!args.help) {
    if (!args.baseUrl) throw new Error("--base-url is required");
    if (!args.paths.length) throw new Error("--paths must contain at least one path");
    if (!args.viewports.length) throw new Error("--viewports must contain at least one viewport");
  }
  return args;
}

function finding(rule, severity, path, viewport, message, details = null) {
  return {rule, severity, path, viewport, message, details};
}

async function loadOptionalDependencies() {
  try {
    const [{chromium}, axeModule] = await Promise.all([import("playwright"), import("@axe-core/playwright")]);
    return {chromium, AxeBuilder: axeModule.default};
  } catch (error) {
    const wrapped = new Error("Optional runtime-audit dependencies are missing. Install them in the target project with: npm install --save-dev playwright @axe-core/playwright");
    wrapped.cause = error;
    throw wrapped;
  }
}

async function auditPage(page, AxeBuilder, path, viewport) {
  const findings = [];
  const consoleErrors = [];
  page.on("console", (message) => { if (message.type() === "error") consoleErrors.push(message.text()); });
  page.on("pageerror", (error) => consoleErrors.push(error.message));
  const axe = await new AxeBuilder({page}).analyze();
  for (const violation of axe.violations) {
    findings.push(finding(`axe.${violation.id}`, violation.impact === "critical" || violation.impact === "serious" ? "warning" : "review", path, viewport, violation.help, {impact: violation.impact, helpUrl: violation.helpUrl, nodes: violation.nodes.length}));
  }
  for (const message of consoleErrors) findings.push(finding("runtime.console-error", "warning", path, viewport, message));
  const layout = await page.evaluate(() => ({scrollWidth: document.documentElement.scrollWidth, clientWidth: document.documentElement.clientWidth}));
  if (layout.scrollWidth > layout.clientWidth + 1) findings.push(finding("runtime.horizontal-overflow", "warning", path, viewport, `Document scrollWidth ${layout.scrollWidth}px exceeds clientWidth ${layout.clientWidth}px.`));
  await page.keyboard.press("Tab");
  const focus = await page.evaluate(() => {
    const element = document.activeElement;
    if (!element) return null;
    const style = getComputedStyle(element);
    return {tag: element.tagName.toLowerCase(), id: element.id || null, role: element.getAttribute("role"), outlineStyle: style.outlineStyle, outlineWidth: style.outlineWidth};
  });
  if (!focus || focus.tag === "body") findings.push(finding("runtime.keyboard-focus-probe", "review", path, viewport, "A first Tab keypress did not move focus to an interactive element. Inspect keyboard order and focusability."));
  return {findings, focus_probe: focus};
}

async function run(args) {
  const {chromium, AxeBuilder} = await loadOptionalDependencies();
  const browser = await chromium.launch({headless: true});
  const results = [];
  const findings = [];
  try {
    for (const viewport of args.viewports) {
      const context = await browser.newContext({viewport, reducedMotion: "reduce"});
      const page = await context.newPage();
      for (const path of args.paths) {
        const url = new URL(path, args.baseUrl).toString();
        const response = await page.goto(url, {waitUntil: "networkidle"});
        if (!response || !response.ok()) {
          findings.push(finding("runtime.navigation", "warning", path, viewport, `Navigation returned ${response ? response.status() : "no response"} for ${url}.`));
          continue;
        }
        const pageResult = await auditPage(page, AxeBuilder, path, viewport);
        findings.push(...pageResult.findings);
        results.push({path, url, viewport, focus_probe: pageResult.focus_probe});
      }
      await context.close();
    }
  } finally { await browser.close(); }
  return {results, findings};
}

async function main() {
  let args;
  try { args = parseArgs(process.argv.slice(2)); }
  catch (error) { console.error(`ERROR: ${error.message}`); console.error(usage()); return 2; }
  if (args.help) { console.log(usage()); return 0; }
  let report;
  try { report = await run(args); }
  catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    if (args.json) console.log(JSON.stringify({tool: "audit_runtime", error: message}, null, 2));
    else console.error(`ERROR: ${message}`);
    return 2;
  }
  const payload = {tool: "audit_runtime", heuristic: true, strict: args.strict, disclaimer: DISCLAIMER, findings: report.findings, pages: report.results};
  if (args.json) console.log(JSON.stringify(payload, null, 2));
  else {
    console.log(DISCLAIMER);
    if (!report.findings.length) console.log("No rendered findings detected by the bundled checks.");
    else {
      for (const item of report.findings) console.log(`${item.severity.toUpperCase().padEnd(7)} ${item.rule} ${item.path} ${item.viewport.width}x${item.viewport.height} - ${item.message}`);
      console.log(`${report.findings.length} finding(s).`);
    }
  }
  return args.strict && report.findings.length ? 1 : 0;
}

process.exitCode = await main();
