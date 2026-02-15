const { ethers } = require('ethers');

async function main() {
    const provider = new ethers.JsonRpcProvider('http://127.0.0.1:8545');
    const shieldAddress = '0x548E337fd6bB26994773179f184ba9a895b5e5c8';

    console.log('--- ARCANA SOVEREIGN DASHBOARD ---');
    console.log('Monitoring Shield at:', shieldAddress);
    console.log('Tracking 136B CC Transaction Limits...');

    provider.on('pending', async (txHash) => {
        const tx = await provider.getTransaction(txHash);
        if (tx && tx.to && tx.to.toLowerCase() === shieldAddress.toLowerCase()) {
            const amount = ethers.formatUnits(tx.value, 18);
            console.log(`[ALERT] Inbound Tx: ${txHash}`);
            console.log(`[DATA] Amount: ${amount} CC`);
            
            if (parseFloat(amount) > 680000000) {
                console.log('\!\!\! CAP VIOLATION DETECTED: EXCEEDS 0.5% \!\!\!');
            }
        }
    });

    console.log('Listening for events... (Press Ctrl+C to stop)');
}

main().catch(console.error);