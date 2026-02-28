const { ethers } = require("ethers");
const fs = require("fs");

async function runSimulation() {
    const provider = new ethers.JsonRpcProvider("http://127.0.0.1:8545");
    const wallet = new ethers.Wallet("YOUR_PRIVATE_KEY", provider);
    
    const totalSwaps = 4500;
    const contractAddr = "0x9a7D8Bd48D046F5D1d4A49c68B89e529eb7587c4";
    const data = "0xa9059cbb0000000000000000000000004654cfdd1a9eaeaa43c985d5dfda6b4297a1e6880000000000000000000000000000000000000000000000000000000000000000";

    let startNonce = await wallet.getNonce();
    console.log(`Starting 4,500 Swaps from Nonce: ${startNonce}`);

    const txs = [];
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
        txs.push(wallet.sendTransaction(tx));
        if (i % 500 === 0) console.log(`Injected ${i} transactions into txpool...`);
    }

    console.log("Awaiting inclusion...");
    await Promise.all(txs);
    console.log("Simulation Complete.");
}

runSimulation();
