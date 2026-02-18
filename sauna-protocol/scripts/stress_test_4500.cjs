const hre = require("hardhat");

async function main() {
  const CC_ADDRESS = "0x6d58FCd2a76E96EEd81fD930bF6712FEDABE403c";
  const SAUNA_ADDRESS = "0xD1dF7ED77228E38C8799e56FaE9E4488ab0C70F2";
  
  const cc = await hre.ethers.getContractAt("CreditCoinPrivate", CC_ADDRESS);
  const sauna = await hre.ethers.getContractAt("SaunaProtocol", SAUNA_ADDRESS);
  
  const totalSwaps = 4500;
  const batchSize = 250; // Reduced to fit the 16.7M gas cap
  const amountPerSwap = hre.ethers.parseUnits("1000", 18);

  console.log("--------------------------------------------------");
  console.log("ARCANA STRESS TEST: 4,500 SWAPS (18 BATCHES OF 250)");
  
  for (let i = 0; i < totalSwaps; i += batchSize) {
    const recipients = Array.from({length: batchSize}, () => hre.ethers.Wallet.createRandom().address);
    console.log(`Processing Batch ${Math.floor(i/batchSize) + 1}/18...`);
    
    // Gas limit set to 15M to stay under the 16.7M cap
    const tx = await sauna.processMassSwaps(recipients, amountPerSwap, {
      gasLimit: 15000000 
    });
    
    const receipt = await tx.wait();
    console.log(`Batch ${Math.floor(i/batchSize) + 1} Success. Gas: ${receipt.gasUsed.toString()}`);
  }

  console.log("SUCCESS: 4,500 swaps confirmed under Gas Cap.");
  console.log("--------------------------------------------------");
}

main().catch((error) => {
  console.error("STRESS TEST FAILED:", error.message);
  process.exitCode = 1;
});
