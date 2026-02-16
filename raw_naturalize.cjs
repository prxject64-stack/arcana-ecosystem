const { ethers } = require("ethers");
const fs = require("fs");
async function main() {
    const provider = new ethers.JsonRpcProvider("http://127.0.0.1:8545");
    const password = "Deezydeezydeezy1$";
    const keystorePath = "data/keystore/UTC--2026-02-16T21-38-36.238816784Z--4f9595e22a0881b1a13f9ac039b45a3eb56d6497";
    const ccAddr = ethers.getAddress("0x39038Ab99d2E2445E336684507d8C392DA41A4bb".toLowerCase());
    const passAddr = ethers.getAddress("0x715cb0edcf88de9f3b1641a40a24ab3d7793dbe0".toLowerCase());
    const json = fs.readFileSync(keystorePath, "utf8");
    const wallet = await ethers.Wallet.fromEncryptedJson(json, password);
    const signer = wallet.connect(provider);
    const ccAbi = ["function approve(address spender, uint256 amount) public returns (bool)"];
    const passAbi = ["function performSacrifice() public"];
    const cc = new ethers.Contract(ccAddr, ccAbi, signer);
    const passport = new ethers.Contract(passAddr, passAbi, signer);
    console.log("1. Approving 100 CC...");
    const tx1 = await cc.approve(passAddr, ethers.parseEther("100"));
    await tx1.wait();
    console.log("Approved! TX:", tx1.hash);
    console.log("2. Executing Sacrifice...");
    const tx2 = await passport.performSacrifice();
    await tx2.wait();
    console.log("--- PEER #1 STATUS: ACTIVE (NATURALIZED) ---");
}
main().catch((err) => { console.error("CRITICAL ERROR:", err.message); });
