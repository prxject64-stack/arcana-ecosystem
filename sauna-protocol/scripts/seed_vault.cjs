const hre = require("hardhat");

async function main() {
  const ccAddress = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512";
  const saunaAddress = "0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0";
  
  const ccToken = await hre.ethers.getContractAt("CreditCoinPrivate", ccAddress);

  console.log("--------------------------------------------------");
  console.log("INITIALIZING LIQUIDITY: 10B CC");

  const amount = hre.ethers.parseUnits("10000000000", 18);
  
  console.log("Transferring 10 Billion CC to Sauna Vault...");
  const tx = await ccToken.transfer(saunaAddress, amount);
  await tx.wait();

  const vaultBal = await ccToken.balanceOf(saunaAddress);
  console.log("SUCCESS: Sauna Vault Seeded.");
  console.log("New Vault Balance:", hre.ethers.formatUnits(vaultBal, 18), "CC");
  console.log("--------------------------------------------------");
}

main().catch(console.error);
