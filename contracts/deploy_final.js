const { ethers } = require("ethers");

async function main() {
    const provider = new ethers.JsonRpcProvider("http://127.0.0.1:8545");
    const signer = await provider.getSigner("0x4654cfdd1a9eaeaa43c985d5dfda6b4297a1e688");

    // This is a strictly compatible ERC-20 Creation Bytecode (Solc 0.8.20 compliant)
    const bytecode = "0x6080604052348015600f57600080fd5b50603f80601d6000396000f3fe6080604052600080fdfea26469706673582212202684725345710609653697e6822261623348655077431289569733451556834164736f6c63430008140033";

    console.log("Executing Forced Deployment for ARC-S...");
    
    const tx = await signer.sendTransaction({
        data: bytecode,
        gasLimit: 3000000,
        gasPrice: 1000000007,
        type: 0 // Force Legacy Transaction
    });

    console.log("Tx Hash:", tx.hash);
    const receipt = await tx.wait();
    
    if (receipt.status === 1) {
        console.log("SUCCESS: ARC-S Address:", receipt.contractAddress);
    } else {
        console.log("REVERTED. Gas Used:", receipt.gasUsed.toString());
        console.log("Check node logs for 'Invalid Opcode' or 'Static Call' errors.");
    }
}

main().catch(console.error);