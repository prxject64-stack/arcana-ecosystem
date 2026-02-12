const ethers = require('ethers');
const fs = require('fs');

async function runTest() {
    // Connect to your local IPC socket
    const provider = new ethers.providers.JsonRpcProvider('http://127.0.0.1:8545');
    const wallet = new ethers.Wallet("YOUR_PRIVATE_KEY", provider);
    
    const targetAddress = "0x70997970C51812dc3A010C7d01b50e0d17dc79C8"; // Example peer
    const amount = ethers.utils.parseUnits("1000", 18); // 1000 CC per swap
    let nonce = await wallet.getTransactionCount();

    console.log(`🚀 Starting 4,500 swaps from Block ${await provider.getBlockNumber()}...`);

    for (let i = 0; i < 4500; i++) {
        const tx = {
            to: targetAddress,
            value: amount,
            nonce: nonce++,
            gasLimit: 21000,
            gasPrice: ethers.utils.parseUnits("20", "gwei")
        };

        wallet.sendTransaction(tx).catch(e => console.error(`Tx ${i} failed`));
        
        if (i % 500 === 0) console.log(`Buffered ${i}/4500 transactions...`);
    }
    console.log("✅ All transactions broadcast to txpool.");
}

runTest();
