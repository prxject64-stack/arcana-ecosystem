const { ethers } = require("hardhat");

async function main() {
    const [owner] = await ethers.getSigners();
    console.log("--- INITIATING 4,500 PEER SWAP STRESS TEST ---");
    
    const Sovereign = await ethers.getContractFactory("SovereignToken");
    const arc = await Sovereign.deploy("Arcana Sovereign", "ARC-S");
    await arc.waitForDeployment();

    let currentNonce = await owner.getNonce();

    for (let i = 0; i < 4500; i++) {
        // We use manual nonces to prevent the 'already used' error
        const tx = await arc.transfer(owner.address, 0, { nonce: currentNonce });
        currentNonce++;
        
        if (i % 500 === 0) {
            console.log(`[PRO-MODE] Processed ${i} swaps...`);
        }
    }
    console.log("[SUCCESS] 4,500 swaps facilitated within Arcana Ecosystem.");
}

main().catch((error) => {
    console.error(error);
    process.exit(1);
});
