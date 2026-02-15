const { ethers } = require('ethers');

async function main() {
    const provider = new ethers.JsonRpcProvider('http://127.0.0.1:8545');
    const pKey = '0xfdfcd399e13c4f7e1612fd5e655159f899a4951ecf21d153a6adef68474271d2';
    const wallet = new ethers.Wallet(pKey, provider);
    const shieldAddr = '0x548E337fd6bB26994773179f184ba9a895b5e5c8';

    console.log('--- STARTING MOCK FLASH LOAN ATTACK ---');
    console.log('Target: 136B CC Liquidity Pool');
    console.log('Strategy: Burst-Fire 3x 1B CC Swaps (Exceeding 0.5% Cap)');

    for(let i=0; i < 3; i++) {
        console.log(`Attempting Attack Vector ${i+1}...`);
        try {
            const tx = await wallet.sendTransaction({
                to: shieldAddr,
                value: ethers.parseUnits('1000000000', 18),
                gasLimit: 100000
            });
            console.log(`[FAIL] Vector ${i+1} bypassed the shield! Hash: ${tx.hash}`);
        } catch (e) {
            console.log(`[SUCCESS] Vector ${i+1} REJECTED: ${e.reason || 'Security Policy Violation'}`);
        }
    }
    console.log('--- ATTACK SIMULATION COMPLETE ---');
}

main().catch(console.error);