const Web3 = require('web3');
const ports = [8545, 8547, 8549];
const amount = "0xde0b6b3a7640000"; // 1 CC in hex

async function flood() {
    for (let i = 0; i < 4500; i++) {
        const port = ports[i % ports.length];
        const web3 = new Web3(`http://127.0.0.1:${port}`);
        // Logic: Send 1 CC to a derived address to stress the TxPool
        web3.eth.sendTransaction({
            from: "0x8d11448f255863E8e4023549297052c4a11DAf13",
            to: "0x323c965BEB3Fa2130a1146ABbE0eA0B20370422D",
            value: amount,
            gas: 21000
        }).catch(e => {}); 
        if (i % 500 === 0) console.log(`Injected ${i} swaps...`);
    }
}
flood();
