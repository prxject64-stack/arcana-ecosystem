const hre = require("hardhat");
async function main() {
  const CC_ADDRESS = "0x6d58FCd2a76E96EEd81fD930bF6712FEDABE403c";
  const SAUNA_ADDRESS = "0xD1dF7ED77228E38C8799e56FaE9E4488ab0C70F2";
  const cc = await hre.ethers.getContractAt("CreditCoinPrivate", CC_ADDRESS);
  const [deployer] = await hre.ethers.getSigners();
  const totalSupply = await cc.totalSupply();
  const vaultBalance = await cc.balanceOf(SAUNA_ADDRESS);
  const deployerBalance = await cc.balanceOf(deployer.address);
  console.log("--------------------------------------------------");
  console.log("ARCANA ECOSYSTEM AUDIT");
  console.log("Total Supply: ", hre.ethers.formatUnits(totalSupply, 18));
  console.log("Vault:        ", hre.ethers.formatUnits(vaultBalance, 18));
  console.log("--------------------------------------------------");
}
main().catch(console.error);
