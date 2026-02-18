const hre = require("hardhat");

async function main() {
  const CC_Factory = await hre.ethers.getContractFactory("CreditCoinPrivate");
  
  const ccAddress = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512";
  const saunaAddress = "0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0";
  const govAddress = "0x322813Fd9A801c5507c9de605d63CEA4f2CE6c44";
  const sentryAddress = "0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9";

  const ccToken = await CC_Factory.attach(ccAddress);
  const [deployer] = await hre.ethers.getSigners();

  const govBal = await ccToken.balanceOf(govAddress);
  const vaultBal = await ccToken.balanceOf(saunaAddress);
  const deployerBal = await ccToken.balanceOf(deployer.address);
  const totalSupply = await ccToken.totalSupply();

  console.log("--------------------------------------------------");
  console.log("ARCANA SOVEREIGN ECOSYSTEM AUDIT [FINALIZED]");
  console.log("Total Supply:     ", hre.ethers.formatUnits(totalSupply, 18), "CC");
  console.log("Sovereign Reserve:", hre.ethers.formatUnits(govBal, 18), "CC (GOV)");
  console.log("Sauna Liquidity:  ", hre.ethers.formatUnits(vaultBal, 18), "CC (VAULT)");
  console.log("Circulating P2P:  ", hre.ethers.formatUnits(totalSupply - govBal - vaultBal, 18), "CC");
  console.log("Deployer Wallet:  ", hre.ethers.formatUnits(deployerBal, 18), "CC (HOT)");
  console.log("--------------------------------------------------");
  console.log("Sentry Guardian:  ", sentryAddress);
  console.log("Governance:       ", govAddress);
}

main().catch(console.error);
