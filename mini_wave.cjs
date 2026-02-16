const { ethers } = require('ethers');
const fs = require('fs');

async function main() {
    const provider = new ethers.JsonRpcProvider('http://127.0.0.1:8545');
    const password = 'Deezydeezydeezy1$';
    const keystorePath = 'data/keystore/UTC--2026-02-16T21-38-36.238816784Z--4f9595e22a0881b1a13f9ac039b45a3eb56d6497';
    
    const peerData = JSON.parse(fs.readFileSync('mini_peers.json', 'utf8'));
    const ccAddr = ethers.getAddress('0x39038Ab99d2E2445E336684507d8C392DA41A4bb'.toLowerCase());
    const ccAbi = ['function transfer(address to, uint256 amount) public returns (bool)'];

    const json = fs.readFileSync(keystorePath, 'utf8');
    const wallet = await ethers.Wallet.fromEncryptedJson(json, password);
    const signer = wallet.connect(provider);
    const cc = new ethers.Contract(ccAddr, ccAbi, signer);

    // Get the next valid nonce including pending txs
    let nonce = await provider.getTransactionCount(wallet.address, 'pending');
    console.log(`Starting at Nonce: ${nonce}`);

    for (let i = 0; i < peerData.length; i++) {
        try {
            const tx = await cc.transfer(peerData[i].address, ethers.parseEther(peerData[i].amount), {
                nonce: nonce++,
                gasLimit: 150000,
                gasPrice: ethers.parseUnits('20', 'gwei') // Forced floor to prevent underpricing
            });
            console.log(`[${i+1}/50] Sent to ${peerData[i].address} | TX: ${tx.hash}`);

            if ((i + 1) % 10 === 0) {
                console.log('Batch reached. Waiting for indexing...');
                let confirmed = false;
                while(!confirmed) {
                    try {
                        await tx.wait();
                        confirmed = true;
                    } catch (e) {
                        if (e.message.includes('indexing')) {
                            await new Promise(r => setTimeout(r, 2000));
                        } else { throw e; }
                    }
                }
            }
            await new Promise(r => setTimeout(r, 200)); 
        } catch (e) {
            if (e.message.includes('underpriced') || e.message.includes('nonce too low')) {
                console.log('Nonce collision detected. Re-syncing...');
                nonce = await provider.getTransactionCount(wallet.address, 'pending');
                i--; // Retry this index
            } else {
                console.error(`CRITICAL ERROR at index ${i}: `, e.message);
                process.exit(1);
            }
        }
    }
    console.log('--- MINI-WAVE COMPLETE: 50 SWAPS SETTLED ---');
}
main();
