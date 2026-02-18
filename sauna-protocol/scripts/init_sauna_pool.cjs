const hre = require("hardhat");

async function main() {
  const CC_ADDRESS = "0x18E317A7D70d8fBf8e6E893616b52390EbBdb629";
  const SAUNA_ADDRESS = "0x4b6aB5F819A515382B0dEB6935D793817bB4af28";
  
  const cc = await hre.ethers.getContractAt("CreditCoinPrivate", CC_ADDRESS);
  const sauna = await hre.ethers.getContractAt("SaunaProtocol", SAUNA_ADDRESS);

  console.log("--------------------------------------------------");
  console.log("ARCANA LIQUIDITY SEEDING");

  // 1. Transfer 10M CC directly to the Sauna Protocol contract
  const seedAmount = hre.ethers.parseUnits("10000000", 18); 
  console.log("Sending 10M CC to Sauna Protocol vault...");
  const transferTx = await cc.transfer(SAUNA_ADDRESS, seedAmount);
  await transferTx.wait();

  // 2. Verify Vault Balance
  const vaultBalance = await cc.balanceOf(SAUNA_ADDRESS);
  console.log("Vault CC Balance:", hre.ethers.formatUnits(vaultBalance, 18), "CC");

  // 3. Prepare 10 recipients for the mass swap test
  const recipients = [];
  for(let i=0; i<10; i++) {
      recipients.push(hre.ethers.Wallet.createRandom().address);
  }

  // 4. Execute processMassSwaps
  const amountPerPerson = hre.ethers.parseUnits("100000", 18); // 100k each
  console.log("Executing processMassSwaps...");
  const tx = await sauna.processMassSwaps(recipients, amountPerPerson);
  await tx.wait();

  console.log("SUCCESS: 1M CC distributed from Vault.");
  console.log("--------------------------------------------------");
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
