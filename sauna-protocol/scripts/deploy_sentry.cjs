const hre = require("hardhat");
async function main() {
  const SAUNA_ADDRESS = "0xD1dF7ED77228E38C8799e56FaE9E4488ab0C70F2";
  const Sentry = await hre.ethers.getContractFactory("ArcanaSentry");
  const sentry = await Sentry.deploy(SAUNA_ADDRESS);
  await sentry.waitForDeployment();
  console.log("Arcana Sentry Deployed to:", await sentry.getAddress());
}
main().catch(console.error);
