const { ethers } = require("ethers");

async function main() {
    const provider = new ethers.JsonRpcProvider("http://127.0.0.1:8545");
    // Use the signer from the provider (unlocked account)
    const signer = await provider.getSigner("0x4654cfdd1a9eaeaa43c985d5dfda6b4297a1e688");

    const bytecode = "0x608060405260008055348015601257600080fd5b5060358060206000396000f3fe6080604052600080fdfea26469706673582212202684725345710609653697e6822261623348655077431289569733451556834164736f6c63430008140033";

    console.log("Sending Raw Transaction via Signer for ARC-S Core...");
    
    const tx = await signer.sendTransaction({
        data: bytecode,
        gasLimit: 2000000,
        gasPrice: 1000000007
    });

    console.log("Transaction Hash:", tx.hash);
    const receipt = await tx.wait();
    
    if (receipt.status === 1) {
        console.log("SUCCESS: ARC-S Root Deployed to:", receipt.contractAddress);
    } else {
        console.log("FAILURE: Transaction reverted.");
        console.log("Gas Used:", receipt.gasUsed.toString());
    }
}

main().catch(console.error);