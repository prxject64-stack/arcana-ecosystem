const hre = require('hardhat');

async function main() {
  const [deployer] = await hre.ethers.getSigners();
  const saUSDAddress = '0x5FbDB2315678afecb367f032d93F642f64180aa3'; // Placeholder
  
  console.log('Deploying SovereignBridge with Swap logic...');
  const Bridge = await hre.ethers.getContractFactory('SovereignBridge');
  const bridge = await Bridge.deploy(saUSDAddress);
  await bridge.waitForDeployment();

  console.log('Bridge deployed to:', await bridge.getAddress());
}

main().catch((error) => { console.error(error); process.exitCode = 1; });
