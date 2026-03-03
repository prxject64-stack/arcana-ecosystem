const Web3 = require('web3');
const web3 = new Web3('http://127.0.0.1:8545');

async function runSwapSimulation() {
    const sender = "0x218e8c79F8a12472a4bA48dd76B55A3e39e40cc8";
    const amount = web3.utils.toWei('1000', 'ether'); // 1000 CC-P per swap
    const totalSwaps = 4500;
    
    console.log(`Initializing 4,500 Swaps from ${sender}...`);
    let nonce = await web3.eth.getTransactionCount(sender);

    for (let i = 0; i < totalSwaps; i++) {
        const tempAccount = web3.eth.accounts.create();
        web3.eth.sendTransaction({
            from: sender,
            to: tempAccount.address,
            value: amount,
            gas: 21000,
            gasPrice: '0',
            nonce: nonce++
        }).on('transactionHash', hash => {
            if (i % 500 === 0) console.log(`Injected ${i} swaps...`);
        });
    }
    console.log("All 4,500 swaps injected into TxPool.");
}

runSwapSimulation();
