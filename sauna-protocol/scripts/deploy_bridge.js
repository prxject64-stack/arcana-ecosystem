const hre = require("hardhat");

async function main() {
  console.log("--- INITIATING OPTIMIZED BRIDGE DEPLOYMENT ---");
  const Bridge = await hre.ethers.getContractFactory("SovereignBridge");
  
  // Explicit gas limit to bypass estimation revert
  const bridge = await Bridge.deploy({ gasLimit: 3000000 });

  await bridge.waitForDeployment();

  console.log(`[SUCCESS] SovereignBridge deployed to: ${await bridge.getAddress()}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
