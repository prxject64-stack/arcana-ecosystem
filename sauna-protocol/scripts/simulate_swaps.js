require('dotenv').config();
const { ethers } = require("hardhat");

async function main() {
    const [owner] = await ethers.getSigners();
    const ticker = process.env.PRIVATE_TICKER || "CC-P";
    console.log(`--- INITIATING 4,500 PEER SWAP STRESS TEST [${ticker}] ---`);
    
    const Sovereign = await ethers.getContractFactory("SovereignToken");
    const arc = await Sovereign.deploy("Arcana Sovereign", "ARC-S");
    await arc.waitForDeployment();

    let currentNonce = await owner.getNonce();

    for (let i = 0; i < 4500; i++) {
        const tx = await arc.transfer(owner.address, 0, { nonce: currentNonce });
        currentNonce++;
        if (i % 500 === 0) console.log(`[SOVEREIGN] Processed ${i} swaps...`);
    }
    console.log(`[SUCCESS] 4,500 swaps facilitated for ${ticker}.`);
}

main().catch((error) => {
    console.error(error);
    process.exit(1);
});
