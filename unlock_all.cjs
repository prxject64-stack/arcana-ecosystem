const { Web3 } = require('web3');
const ports = [8545, 8547, 8549];
const address = "0x8d11448f255863e8e4023549297052c4a11daf13";
const password = "YOUR_PASSWORD"; // Replace with your actual password

async function unlock() {
    for (const port of ports) {
        const web3 = new Web3(`http://127.0.0.1:${port}`);
        try {
            // Using raw RPC call to bypass 'personal' variable undefined in console
            const result = await web3.currentProvider.request({
                method: 'personal_unlockAccount',
                params: [address.toLowerCase(), password, 3600]
            });
            console.log(`Node ${port}: Unlock Successful -> ${result}`);
        } catch (e) {
            console.error(`Node ${port}: Unlock Failed. Error: ${e.message}`);
            console.log(`HINT: Restart Peer at ${port} with --http.api eth,net,web3,personal --allow-insecure-unlock`);
        }
    }
}
unlock();
