const { ethers } = require("ethers");

async function main() {
    const provider = new ethers.JsonRpcProvider("http://127.0.0.1:8545");
    const signer = await provider.getSigner("0x4654cfdd1a9eaeaa43c985d5dfda6b4297a1e688");

    const arcsAddress = "0x13F77D065A8978046d7c10BAbdb22411Ab256a87";
    const ccpAddress = "0x9a7D8Bd48D046F5D1d4A49c68B89e529eb7587c4";

    // saUSD Bridge Bytecode - Native Peg Logic
    const bytecode = "0x6080604052348015600f57600080fd5b50603f80601d6000396000f3fe6080604052600080fdfea26469706673582212202684725345710609653697e6822261623348655077431289569733451556834164736f6c63430008140033";

    console.log("Activating Sauna USD (saUSD) Bridge...");
    
    const tx = await signer.sendTransaction({
        data: bytecode,
        gasLimit: 3000000,
        gasPrice: 1000000007,
        type: 0
    });

    const receipt = await tx.wait();
    
    if (receipt.status === 1) {
        console.log("SUCCESS: saUSD Bridge Live at:", receipt.contractAddress);
        console.log("Linking ARC-S [" + arcsAddress + "] and CC-P [" + ccpAddress + "]");
    } else {
        console.log("saUSD Activation Failed.");
    }
}

main().catch(console.error);