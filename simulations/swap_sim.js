const { ethers } = require("ethers");

async function runSimulation() {
    // Connect to Peer 2
    const provider = new ethers.JsonRpcProvider("http://127.0.0.1:8545");
    
    // Using your known account
    const privateKey = "0xfdfcd399e13c4f7e1612fd5e655159f899a4951ecf21d153a6adef68474271d2"; 
    const wallet = new ethers.Wallet(privateKey, provider);
    
    const totalSwaps = 4500;
    const contractAddr = "0x9a7D8Bd48D046F5D1d4A49c68B89e529eb7587c4";
    
    // Transfer selector: 0xa9059cbb (Amount: 0 for stress test)
    const data = "0xa9059cbb0000000000000000000000004654cfdd1a9eaeaa43c985d5dfda6b4297a1e6880000000000000000000000000000000000000000000000000000000000000000";

    let startNonce = await wallet.getNonce();
    console.log("Network: Arcana Sovereign (ChainID 136)");
    console.log("Target: " + contractAddr);
    console.log("Starting 4,500 Swaps from Nonce: " + startNonce);

    for (let i = 0; i < totalSwaps; i++) {
        const tx = {
            to: contractAddr,
            data: data,
            gasLimit: 100000,
            maxPriorityFeePerGas: ethers.parseUnits("2", "gwei"),
            maxFeePerGas: ethers.parseUnits("100", "gwei"),
            nonce: startNonce + i,
            chainId: 136
        };
        
        // Send and don't wait (Fire and Forget to fill mempool)
        wallet.sendTransaction(tx).catch(err => console.error("Tx " + i + " failed: " + err.message));
        
        if (i % 500 === 0) {
            console.log("Injected " + i + " transactions into txpool...");
        }
    }

    console.log("All transactions broadcasted. Monitor Geth console with: txpool.status");
}

runSimulation().catch(console.error);
