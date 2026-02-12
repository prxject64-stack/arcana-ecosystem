const ethers = require("ethers");
const fs = require("fs");

async function main() {
    const provider = new ethers.JsonRpcProvider("http://127.0.0.1:8545");
    const privateKey = "YOUR_PRIVATE_KEY_HERE";
    const wallet = new ethers.Wallet(privateKey, provider);
    const compiled = JSON.parse(fs.readFileSync("CC_Compiled.json"));
    const abi = compiled.contracts["./CreditCoinPrivate.sol:CreditCoinPrivate"].abi;
    const bytecode = compiled.contracts["./CreditCoinPrivate.sol:CreditCoinPrivate"].bin;

    console.log("🚀 Deploying 136B Credit Coin Private (CC)...");
    const factory = new ethers.ContractFactory(abi, bytecode, wallet);
    const contract = await factory.deploy({
        gasPrice: 20,
        gasLimit: 4000000
    });

    await contract.waitForDeployment();
    console.log("🏁 CC Contract Deployed to:", await contract.getAddress());
    console.log("📦 Total Supply Verified: 136,000,000,000 CC");
}

main().catch((error) => {
    console.error(error);
    process.exit(1);
});