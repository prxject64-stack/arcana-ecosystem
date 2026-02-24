const crypto = require('crypto');
const fs = require('fs');

const path = "/root/arcana-ecosystem/arcana_data/keystore/UTC--2026-02-24T03-24-11.552875466Z--c4bbb118acc45f1be50de724f1757b1a19e19de3";
const password = "Arcana2026!";

try {
    const content = JSON.parse(fs.readFileSync(path, 'utf8'));
    const kdfparams = content.crypto.kdfparams;
    const ciphertext = Buffer.from(content.crypto.ciphertext, 'hex');
    const iv = Buffer.from(content.crypto.cipherparams.iv, 'hex');
    const salt = Buffer.from(kdfparams.salt, 'hex');
    const targetMac = content.crypto.mac;

    // 1. Derive the key using scrypt
    const derivedKey = crypto.scryptSync(password, salt, kdfparams.dklen, {
        N: kdfparams.n,
        r: kdfparams.r,
        p: kdfparams.p,
        maxmem: 128 * 1024 * 1024 * 1024 // Adjust if needed
    });

    // 2. Verify MAC (Standard V3 procedure)
    const validate = Buffer.concat([derivedKey.slice(16, 32), ciphertext]);
    const mac = crypto.createHash('sha3-256').update(validate).digest('hex');

    if (mac !== targetMac) {
        throw new Error("MAC mismatch: Incorrect password or corrupted file.");
    }

    // 3. Decrypt ciphertext using AES-128-CTR
    const decipher = crypto.createDecipheriv('aes-128-ctr', derivedKey.slice(0, 16), iv);
    const privateKey = Buffer.concat([decipher.update(ciphertext), decipher.final()]);

    console.log("\nSUCCESS");
    console.log("PRIVATE_KEY: 0x" + privateKey.toString('hex'));
} catch (err) {
    console.error("\nFAILURE: " + err.message);
    process.exit(1);
}
