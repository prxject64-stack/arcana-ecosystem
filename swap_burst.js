const { ethers } = require('ethers');

async function runTest() {
    try {
        // Connect to local node (v6 syntax)
        const provider = new ethers.JsonRpcProvider('http://127.0.0.1:8545');
        
        // Load the 136B CC Key
        const pKey = process.env.ARCANA_KEY;
        if (!pKey) {
            console.error("❌ CRITICAL: ARCANA_KEY environment variable is missing.");
            process.exit(1);
        }
        
        const wallet = new ethers.Wallet(pKey, provider);
        const targetAddress = "0x70997970C51812dc3A010C7d01b50e0d17dc79C8"; 
        
        // v6 uses ethers.parseUnits directly (no .utils)
        const amount = ethers.parseUnits("1000", 18); 
        
        console.log(`🚀 STARTING BURST: 4,500 Swaps from Block ${await provider.getBlockNumber()}...`);
        
        // optimized nonce management
        let nonce = await wallet.getNonce(); 

        const txs = [];
        for (let i = 0; i < 4500; i++) {
            const tx = {
                to: targetAddress,
                value: amount,
                nonce: nonce++,
                gasLimit: 21000,
                gasPrice: ethers.parseUnits("20", "gwei")
            };

            // Send without waiting (Fire and Forget)
            txs.push(wallet.sendTransaction(tx).catch(e => console.error(`Tx ${i} Error: ${e.message}`)));
            
            if (i % 500 === 0) console.log(`Buffered ${i}/4500 transactions...`);
        }
        
        await Promise.all(txs);
        console.log("✅ EXECUTION COMPLETE: 4,500 Transactions broadcast to Mempool.");

    } catch (error) {
        console.error("FATAL ERROR:", error);
    }
}

runTest();
