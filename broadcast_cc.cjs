const { ethers } = require("ethers");
const fs = require("fs");

async function main() {
    const provider = new ethers.JsonRpcProvider("http://127.0.0.1:8545");
    const privateKey = "0xfdfcd399e13c4f7e1612fd5e655159f899a4951ecf21d153a6adef68474271d2";
    const wallet = new ethers.Wallet(privateKey, provider);

    // We will reuse the same compiled DNA but change the internal state via the constructor if needed
    // For now, we deploy the CC instance
    const artifact = JSON.parse(fs.readFileSync("./artifacts/ArcanaSovereign.json", "utf8"));
    const factory = new ethers.ContractFactory(artifact.abi, artifact.evm.bytecode.object, wallet);

    console.log("Broadcasting Credit Coin Private (CC)...");
    const contract = await factory.deploy();
    await contract.waitForDeployment();

    console.log("-----------------------------------------");
    console.log("SUCCESS: CC PRIVATE IS LIVE");
    console.log("CONTRACT ADDRESS:", await contract.getAddress());
    console.log("-----------------------------------------");
}

main().catch(console.error);
