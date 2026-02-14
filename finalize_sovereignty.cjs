const { ethers } = require("ethers");

async function main() {
    const provider = new ethers.JsonRpcProvider("http://127.0.0.1:8545");
    const privateKey = "0xfdfcd399e13c4f7e1612fd5e655159f899a4951ecf21d153a6adef68474271d2";
    const masterWallet = new ethers.Wallet(privateKey, provider);
    
    // Lowercased to bypass Ethers.js v6 checksum strictness
    const securityWallet = "0xc3129faee7770565cc7ca1fd88e337fd6bb26994"; 
    
    console.log("Good To GO: Initializing 40B ETH transfer to Security Vault...");

    const tx = await masterWallet.sendTransaction({
        to: securityWallet,
        value: ethers.parseEther("40000000000")
    });

    console.log("Transaction Broadcast. Hash: " + tx.hash);
    console.log("Waiting for block confirmation...");
    await tx.wait();
    
    const finalBalance = await provider.getBalance(securityWallet);
    console.log("-----------------------------------------");
    console.log("SAUNA PROTOCOL FUNDED");
    console.log("Security Wallet: " + securityWallet);
    console.log("Security Wallet Balance: " + ethers.formatEther(finalBalance) + " ETH");
    console.log("-----------------------------------------");
}

main().catch((err) => {
    console.error("Critical Failure:", err);
    process.exit(1);
});
