const { ethers } = require('ethers');
const fs = require('fs');

async function decrypt() {
    const keystorePath = './arcana_data/keystore/UTC--2026-02-12T01-36-58.431883549Z--14a3256052c02f9d87fe1cc3b712d4530061b25c';
    const json = fs.readFileSync(keystorePath, 'utf8');
    const password = 'Deezydeezydeezy1$'; // Replace with your actual password

    console.log("⏳ Decrypting... (This can take up to 60s due to Scrypt difficulty)");
    
    try {
        const wallet = await ethers.Wallet.fromEncryptedJson(json, password);
        console.log("\n✅ SUCCESS");
        console.log("PRIVATE_KEY=" + wallet.privateKey);
    } catch (e) {
        console.error("\n❌ Decryption failed: Check your password.");
    }
}

decrypt();
