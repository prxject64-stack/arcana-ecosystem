import hre from 'hardhat';

async function main() {
  const [deployer] = await hre.ethers.getSigners();
  console.log('--------------------------------------------------');
  console.log('DEPLOΥING SAUNA STABILITY LOOP');
  console.log('Deployer:', deployer.address);
  
  const sUSD = await hre.ethers.deployContract('SovereignDollar');
  await sUSD.waitForDeployment();
  const sUSDAddress = await sUSD.getAddress();
  console.log('sUSD deployed to:', sUSDAddress);

  const ARC_ADDRESS = '0x3BDa2C9D146Cf23B6EE1AE51bEEc6308B309b690';
  const Vault = await hre.ethers.deployContract('SaunaVault', [sUSDAddress, ARC_ADDRESS]);
  await Vault.waitForDeployment();
  const vaultAddress = await Vault.getAddress();
  console.log('SaunaVault deployed to:', vaultAddress);
  console.log('--------------------------------------------------');
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
