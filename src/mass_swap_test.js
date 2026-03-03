const { ethers } = require("ethers");

async function main() {
    const provider = new ethers.JsonRpcProvider("http://127.0.0.1:8545");
    const signer = await provider.getSigner("0x4654cfdd1a9eaeaa43c985d5dfda6b4297a1e688");
    const saunaAddress = "0xf225E92458B73F1A0E872c2F6597B8141F669Cca";

    const abi = ["function processMassSwaps(address[] recipients, uint256 amount)"];
    const contract = new ethers.Contract(saunaAddress, abi, signer);

    const rawRecipients = [
        "0x70997970C51812dc3A010C7d01b50e0d17dc79C8",
        "0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC",
        "0x90F79bf6EB2c4f870365E785982E1f101E93b906",
        "0x15d34AAf54267DB7D7c367839AAf71A00a2C6A65",
        "0x9965507D1a55bcC2695C58ba16FB37d819B0A4df"
    ];

    // Normalize to lowercase to bypass EIP-55 Checksum validation
    const recipients = rawRecipients.map(addr => addr.toLowerCase());
    
    const amountPerPeer = ethers.parseEther("100000"); 

    console.log("Initiating Mass Swap for 5 test peers (Normalized)...Metadata: Bypassing Checksum.");
    const tx = await contract.processMassSwaps(recipients, amountPerPeer);
    await tx.wait();
    console.log("SUCCESS: 500,000 CC Distributed. Tx Hash:", tx.hash);
}

main().catch(console.error);