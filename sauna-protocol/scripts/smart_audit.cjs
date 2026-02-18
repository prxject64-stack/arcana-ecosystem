const hre = require("hardhat");

async function main() {
  const CC_Factory = await hre.ethers.getContractFactory("CreditCoinPrivate");
  const Sauna_Factory = await hre.ethers.getContractFactory("SaunaProtocol");
  const Sentry_Factory = await hre.ethers.getContractFactory("ArcanaSentry");

  const ccAddress = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512";
  const saunaAddress = "0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0";
  const sentryAddress = "0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9";

  const ccToken = await CC_Factory.attach(ccAddress);
  const sauna = await Sauna_Factory.attach(saunaAddress);
  const sentry = await Sentry_Factory.attach(sentryAddress);

  const [deployer] = await hre.ethers.getSigners();
  const bal = await ccToken.balanceOf(deployer.address);
  const vaultBal = await ccToken.balanceOf(saunaAddress);

  console.log("--------------------------------------------------");
  console.log("ARCANA SYSTEM STATUS [LIVE]");
  console.log("CC Token:      ", ccAddress);
  console.log("Deployer Bal:  ", hre.ethers.formatUnits(bal, 18), "CC");
  console.log("Sauna Vault:   ", hre.ethers.formatUnits(vaultBal, 18), "CC");
  console.log("Sentry Active: ", sentryAddress);
  console.log("--------------------------------------------------");
}

main().catch(console.error);
