const { Web3 } = require('web3');
const ports = [8545, 8547, 8549];
// Force lowercase to pass strict validation
const sender = "0x8d11448f255863e8e4023549297052c4a11daf13".toLowerCase();
const receiver = "0x323c965beb3fa2130a1146abbe0ea0b20370422d".toLowerCase();

async function flood() {
    const web3 = new Web3(`http://127.0.0.1:8545`);
    const startNonce = await web3.eth.getTransactionCount(sender);
    console.log(`Igniting Sauna: 4,500 swaps from Nonce ${startNonce}`);

    for (let i = 0; i < 4500; i++) {
        const port = ports[i % ports.length];
        const provider = new Web3(`http://127.0.0.1:${port}`);
        
        provider.eth.sendTransaction({
            from: sender,
            to: receiver,
            value: "0xde0b6b3a7640000",
            gas: 21000,
            nonce: Number(startNonce) + i
        }).catch(() => {}); // Burn errors to maintain injection speed

        if (i % 500 === 0) console.log(`Injected ${i} / 4500...`);
    }
}
flood();
