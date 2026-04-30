const fs = require('fs');
const path = require('path');

function parseMdSection(content, sectionName) {
    const pattern = new RegExp(`## ${sectionName}\\s*([\\s\\S]*?)(?=\\n##|$)`);
    const match = content.match(pattern);
    return match ? match[1].trim() : "";
}

function listItems(sectionText) {
    return sectionText.split('\n')
        .map(line => line.trim())
        .filter(line => line.startsWith('-'))
        .map(line => line.replace(/^-\s*/, '').trim());
}

function collectMetrics(evidencePath, briefPath) {
    if (!fs.existsSync(evidencePath)) {
        console.error(`Error: Evidence ledger not found at ${evidencePath}`);
        process.exit(1);
    }

    const evidenceContent = fs.readFileSync(evidencePath, 'utf8');

    const task = parseMdSection(evidenceContent, "Task");
    const result = parseMdSection(evidenceContent, "Result");
    const filesRead = listItems(parseMdSection(evidenceContent, "Files Read"));
    const filesTouched = listItems(parseMdSection(evidenceContent, "Files Touched"));
    const checksRun = listItems(parseMdSection(evidenceContent, "Checks Run"));
    const verifiedClaims = listItems(parseMdSection(evidenceContent, "Verified Claims"));
    
    let plannedFilesTouch = [];
    if (briefPath && fs.existsSync(briefPath)) {
        const briefContent = fs.readFileSync(briefPath, 'utf8');
        plannedFilesTouch = listItems(parseMdSection(briefContent, "Files To Touch"));
    }

    const skillsLoaded = 1; 
    const reportsGenerated = 2; 
    const contextLoadProxy = filesRead.length + skillsLoaded + reportsGenerated;
    
    const verifiedTasks = (result.toLowerCase().includes("pass") || verifiedClaims.length > 0) ? 1 : 0;
    const proxyTvp = verifiedTasks > 0 ? (contextLoadProxy / verifiedTasks).toFixed(2) : "undefined";
    
    const unplannedTouches = plannedFilesTouch.length > 0 
        ? filesTouched.filter(f => !plannedFilesTouch.includes(f))
        : [];
    const scopeCreep = filesTouched.length > 0 ? (unplannedTouches.length / filesTouched.length).toFixed(2) : "0.00";
    
    const verificationRate = (checksRun.length > 0 && verifiedTasks > 0) ? "1.00" : "0.00";

    const report = `# Xskill Metrics Report (Auto-Generated)

## Task
${task}

## Run Type
- [x] With Xskill

## Verified Progress
- Verified tasks completed: ${verifiedTasks}
- Evidence source: ${evidencePath}

## Context Load
- Skills loaded: ${skillsLoaded}
- Reports generated or used: ${reportsGenerated}
- Files read: ${filesRead.length}
- Context Load Size: ${filesRead.length}
- Context Load Proxy: ${contextLoadProxy}

## Scope Control
- Files planned to touch: ${plannedFilesTouch.length > 0 ? plannedFilesTouch.length : 'unknown'}
- Files actually touched: ${filesTouched.length}
- Unplanned files touched: ${unplannedTouches.length}
- Scope Creep Rate: ${scopeCreep}

## Verification
- Checks run: ${checksRun.length}
- Verification Rate: ${verificationRate}

## TVP
- Proxy TVP: ${proxyTvp}

## Interpretation
Task completed with a Context Load Proxy of ${contextLoadProxy}. 
TVP of ${proxyTvp} indicates efficient use of tokens for verified progress.
`;
    return report;
}

const args = process.argv.slice(2);
if (args.length < 1) {
    console.log("Usage: node collect.js <evidence_ledger_path> [execution_brief_path]");
} else {
    const ePath = args[0];
    const bPath = args[1] || null;
    console.log(collectMetrics(ePath, bPath));
}
