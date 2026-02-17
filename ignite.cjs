const { Web3 } = require('web3');
const ports = [8545, 8547, 8549];
const sender = "0x8d11448f255863e8e4023549297052c4a11daf13".toLowerCase();
const receiver = "0x323c965beb3fa2130a1146abbe0ea0b20370422d".toLowerCase();

async function flood() {
    // Connect to Peer 1 to fetch the starting nonce
    const web3 = new Web3(`http://127.0.0.1:8545`);
    let currentNonce;
    try {
        currentNonce = Number(await web3.eth.getTransactionCount(sender));
        console.log(`Atomic Ignition: Starting from Nonce ${currentNonce}`);
    } catch (e) {
        console.error("Failed to connect to Node. Is Peer 1 running on 8545?");
        return;
    }

    for (let i = 0; i < 4500; i++) {
        const port = 8545;
        const provider = new Web3(`http://127.0.0.1:${port}`);
        
        provider.eth.sendTransaction({
            from: sender,
            to: receiver,
            value: "0xde0b6b3a7640000", // 1 ARC/CC
            gas: 21000,
            nonce: currentNonce + i
        }).catch(e => {
            if (i % 1000 === 0) console.log(`Injection ${i} logged: ${e.message.substring(0, 50)}`);
        });

        if (i % 500 === 0) console.log(`Injected ${i} / 4500 swaps...`);
    }
    console.log(`Flood complete. Target final Nonce: ${currentNonce + 4500}`);
}

flood();
