const { ethers } = require("ethers");
const fs = require("fs");

async function main() {
    const RPC_URL = "http://127.0.0.1:8545";
    const provider = new ethers.JsonRpcProvider(RPC_URL);
    const signer = await provider.getSigner("0xbdae565eff11d46dfd2154442f0a565b4011f3b8");

    console.log(`\n--- Arcana Atomic Deployment ---`);
    console.log(`Signer: ${signer.address}`);

    // Minimalist ABI
    const abi = [
        "function deposit() public payable",
        "function balance() public view returns (uint256)"
    ];

    // Verified simple storage bytecode
    const bytecode = "0x6080604052348015600f57600080fd5b5060728061001e6000396000f3fe6080604052348015600f57600080fd5b6004361060325760003560e01c806327e235e3146037578063b69ef8a814604b575b600080fd5b3460008082825401925050819055506049565b005b60005460405190815260200160405180910390f3fea264697066735822122097746269";

    const factory = new ethers.ContractFactory(abi, bytecode, signer);

    try {
        console.log("Submitting Atomic Vault (Limit: 2,000,000 Gas)...");
        // Setting a reasonable limit. If it hits 2M, we know it's a code issue.
        const contract = await factory.deploy({ gasLimit: 2000000 });

        console.log("Transaction Hash:", contract.deploymentTransaction().hash);
        await contract.waitForDeployment();
        
        const address = await contract.getAddress();
        console.log("\n===============================================");
        console.log(`SUCCESS: Atomic Vault Deployed at: ${address}`);
        console.log("===============================================\n");

        fs.writeFileSync("deployed_address.txt", address);
    } catch (error) {
        console.error("Deployment Failed.");
        console.error("Details:", error.message);
    }
}

main();
