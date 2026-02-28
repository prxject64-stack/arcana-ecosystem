const { ethers } = require('ethers');

async function main() {
    const provider = new ethers.JsonRpcProvider('http://127.0.0.1:8545');
    // Using your unlocked account from the node logs
    const signer = await provider.getSigner('0x4654cfdd1a9eaeaa43c985d5dfda6b4297a1e688');
    const contractAddress = '0x9a7D8Bd48D046F5D1d4A49c68B89e529eb7587c4';

    console.log('Commencing 4500 CC-P swaps on Arcana Sovereign...');
    
    // Fetch nonce once and handle increments locally for speed
    let nonce = await provider.getTransactionCount(signer.address);

    for (let i = 0; i < 4500; i++) {
        const tx = {
            to: contractAddress,
            value: 0,
            gasLimit: 60000, 
            gasPrice: ethers.parseUnits('20', 'gwei'),
            nonce: nonce++,
            data: '0x' 
        };

        // Fire-and-forget to maximize throughput
        signer.sendTransaction(tx).catch(err => {
            if (!err.message.includes('already known')) {
                console.error('Tx ' + i + ' Error:', err.message);
            }
        });

        if (i % 500 === 0) console.log('Dispatched ' + i + ' swaps...');
    }
    console.log('All 4500 transactions dispatched to the pool.');
}

main().catch(console.error);
