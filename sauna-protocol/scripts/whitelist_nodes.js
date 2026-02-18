const fs = require('fs');

const distressedNodes = [
    { name: "Kwenta", reason: "Perp Liquidity Crisis", priority: "Critical" },
    { name: "Curve_LP_sUSD", reason: "Impermanent Loss > 20%", priority: "High" },
    { name: "Aave_sUSD_Pool", reason: "Bad Debt Accumulation", priority: "High" },
    { name: "DAXA_Exchanges", reason: "Regulatory Warning", priority: "Medium" }
];

console.log("--- GENERATING SOVEREIGN INVITATION LIST ---");
distressedNodes.forEach(node => {
    console.log(`[TARGET] ${node.name} | Status: ${node.priority} | Issue: ${node.reason}`);
});

fs.writeFileSync('target_nodes.json', JSON.stringify(distressedNodes, null, 2));
