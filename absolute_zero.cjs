const { Web3 } = require('web3');
const web3 = new Web3(`http://127.0.0.1:8545`);
const sender = "0x8d11448f255863e8e4023549297052c4a11daf13".toLowerCase();
const receiver = "0x323c965beb3fa2130a1146abbe0ea0b20370422d".toLowerCase();

async function stressTest() {
    let currentNonce = Number(await web3.eth.getTransactionCount(sender));
    console.log(`Starting 100,000 Swap Flood at Nonce: ${currentNonce}`);
    
    for (let i = 0; i < 100000; i++) {
        web3.eth.sendTransaction({
            from: sender,
            to: receiver,
            value: web3.utils.toWei("1", "ether"),
            gas: 21000,
            nonce: currentNonce + i
        }).catch(e => {
            if (i % 5000 === 0) console.error(`Batch Error at ${i}: ${e.message}`);
        });

        if (i % 10000 === 0) {
            console.log(`Injected ${i} / 100,000 transactions...`);
        }
    }
    console.log(`Flood Sent. Target Nonce: ${currentNonce + 100000}`);
}

stressTest();
