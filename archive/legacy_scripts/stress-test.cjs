const ethers = require('ethers');
const fs = require('fs');

async function runNaturalization() {
    const RPC_URL = "http://127.0.0.1:8545"; 
    const PRIVATE_KEY = process.env.PK; 
    if (!PRIVATE_KEY) { console.error("Error: export PK=your_key first."); process.exit(1); }

    const provider = new ethers.JsonRpcProvider(RPC_URL);
    const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

    const addresses = fs.readFileSync('citizenship-grant-list.txt', 'utf8')
                        .split('\n')
                        .map(a => a.trim())
                        .filter(addr => addr.startsWith('0x'));

    console.log("--- ARCANA NATURALIZATION CEREMONY STARTING ---");
    console.log("Targeting " + addresses.length + " Residents");

    let nonce = await wallet.getNonce();

    for (let i = 0; i < addresses.length; i++) {
        const tx = {
            to: addresses[i],
            value: ethers.parseEther("0.0001"), 
            data: ethers.id("ARCANA_CITIZENSHIP_GRANT_V1"), 
            nonce: nonce++
        };

        try {
            const sentTx = await wallet.sendTransaction(tx);
            console.log("[" + (i+1) + "/" + addresses.length + "] Sent: " + sentTx.hash);
            if (i % 50 === 0) await new Promise(r => setTimeout(r, 100)); 
        } catch (err) {
            console.error("Failed at " + addresses[i] + ": " + err.message);
        }
    }
}
runNaturalization();
