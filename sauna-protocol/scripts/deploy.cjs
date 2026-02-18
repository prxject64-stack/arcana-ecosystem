const hre = require("hardhat");
async function main() {
  const CC = await hre.ethers.getContractFactory("CreditCoinPrivate");
  const cc = await CC.deploy();
  await cc.waitForDeployment();
  const ccAddress = await cc.getAddress();

  const Sauna = await hre.ethers.getContractFactory("SaunaProtocol");
  const sauna = await Sauna.deploy(ccAddress);
  await sauna.waitForDeployment();

  console.log("CC Deployed to:", ccAddress);
  console.log("Sauna Deployed to:", await sauna.getAddress());
}
main().catch(console.error);
