const hre = require("hardhat");

async function main() {
  const CC_ADDRESS = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512";
  const SAUNA_ADDRESS = "0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0";
  
  const sauna = await hre.ethers.getContractAt("SaunaProtocol", SAUNA_ADDRESS);
  
  const totalSwaps = 4500;
  const batchSize = 250; 
  const amountPerSwap = hre.ethers.parseUnits("1000", 18);

  console.log("--------------------------------------------------");
  console.log("EXECUTING ARCANA 4,500 SWAP PRODUCTION TEST");
  
  for (let i = 0; i < totalSwaps; i += batchSize) {
    const recipients = Array.from({length: batchSize}, () => hre.ethers.Wallet.createRandom().address);
    console.log(`Processing Batch ${Math.floor(i/batchSize) + 1}/18...`);
    
    const tx = await sauna.processMassSwaps(recipients, amountPerSwap, {
      gasLimit: 15000000 
    });
    
    const receipt = await tx.wait();
    console.log(`Batch ${Math.floor(i/batchSize) + 1} Success. Gas: ${receipt.gasUsed.toString()}`);
  }

  console.log("SUCCESS: 4.5M CC Circulated via 4,500 Swaps.");
  console.log("--------------------------------------------------");
}

main().catch(console.error);
