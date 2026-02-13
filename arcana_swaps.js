const { Web3 } = require('web3'); // Must use curly braces for v4+
const web3 = new Web3('http://127.0.0.1:8545');

const SENDER = "0x8f7F9762C953Ea6190B541603513a86377eD0767";
const TOTAL_CC = 135999999999;
const PEER_COUNT = 4500;
const AMOUNT_PER_PEER = web3.utils.toWei((TOTAL_CC / PEER_COUNT).toFixed(18), "ether");

async function executeSwaps() {
    try {
        let nonce = await web3.eth.getTransactionCount(SENDER);
        console.log(`Initial Nonce: ${nonce} | Allocation: ${AMOUNT_PER_PEER} Wei`);

        for (let i = 0; i < PEER_COUNT; i++) {
            let tempAccount = web3.eth.accounts.create(); 
            
            web3.eth.sendTransaction({
                from: SENDER,
                to: tempAccount.address,
                value: AMOUNT_PER_PEER,
                gas: 21000,
                nonce: nonce++,
                gasPrice: await web3.eth.getGasPrice()
            }).catch(e => console.error(`Tx ${i} failed:`, e.message));

            if (i % 500 === 0) console.log(`Queued ${i}/4500 transactions...`);
            await new Promise(resolve => setTimeout(resolve, 10)); 
        }
        console.log("All 4,500 transactions broadcast to the mempool.");
    } catch (error) {
        console.error("Master Script Error:", error);
    }
}
executeSwaps();
