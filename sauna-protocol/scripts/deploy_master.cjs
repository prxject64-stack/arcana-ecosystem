const hre = require("hardhat");

async function main() {
  console.log("--------------------------------------------------");
  console.log("RESTORING ARCANA ECOSYSTEM...");

  const CC = await hre.ethers.getContractFactory("CreditCoinPrivate");
  const cc = await CC.deploy();
  await cc.waitForDeployment();
  const ccAddress = await cc.getAddress();
  console.log("1. CC (136B) Deployed to:", ccAddress);

  const Sauna = await hre.ethers.getContractFactory("SaunaProtocol");
  const sauna = await Sauna.deploy(ccAddress);
  await sauna.waitForDeployment();
  const saunaAddress = await sauna.getAddress();
  console.log("2. Sauna Protocol Deployed to:", saunaAddress);

  const Sentry = await hre.ethers.getContractFactory("ArcanaSentry");
  const sentry = await Sentry.deploy(saunaAddress);
  await sentry.waitForDeployment();
  console.log("3. Arcana Sentry Deployed to:", await sentry.getAddress());
  console.log("--------------------------------------------------");
}

main().catch(console.error);
