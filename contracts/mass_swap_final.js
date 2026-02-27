const { ethers } = require("ethers");
const fs = require("fs");

async function main() {
    const provider = new ethers.JsonRpcProvider("http://127.0.0.1:8545");
    const signer = await provider.getSigner("0x4654cfdd1a9eaeaa43c985d5dfda6b4297a1e688");
    const saunaAddress = "0xf225E92458B73F1A0E872c2F6597B8141F669Cca";
    const abi = ["function processMassSwaps(address[] recipients, uint256 amount)"];
    const contract = new ethers.Contract(saunaAddress, abi, signer);

    // Load the 4,500 addresses (assumes a file named addresses.json exists)
    const allAddresses = JSON.parse(fs.readFileSync("addresses.json"));
    const batchSize = 500;
    const amountPerPeer = ethers.parseEther("100000");

    for (let i = 0; i < allAddresses.length; i += batchSize) {
        const batch = allAddresses.slice(i, i + batchSize).map(a => a.toLowerCase());
        console.log(`Processing batch ${i / batchSize + 1} of ${Math.ceil(allAddresses.length / batchSize)}...`);
        const tx = await contract.processMassSwaps(batch, amountPerPeer);
        await tx.wait();
        console.log(`Batch ${i / batchSize + 1} SUCCESS. Hash: ${tx.hash}`);
    }
}

main().catch(console.error);