const crypto = require('crypto');
const fs = require('fs');

const path = "/root/arcana-ecosystem/arcana_data/keystore/UTC--2026-02-24T03-24-11.552875466Z--c4bbb118acc45f1be50de724f1757b1a19e19de3";
const candidates = [
    "Arcana2026!",
    "arcana2026",
    "Deezydeezydeezy1$",
    "YOUR_SAVED_PASSWORD",
    "password",
    "changeit",
    ""
];

const content = JSON.parse(fs.readFileSync(path, 'utf8'));
const kdfparams = content.crypto.kdfparams;
const ciphertext = Buffer.from(content.crypto.ciphertext, 'hex');
const salt = Buffer.from(kdfparams.salt, 'hex');
const targetMac = content.crypto.mac;

candidates.forEach(password => {
    try {
        const derivedKey = crypto.scryptSync(password, salt, kdfparams.dklen, {
            N: kdfparams.n, r: kdfparams.r, p: kdfparams.p,
            maxmem: 1024 * 1024 * 1024
        });
        const validate = Buffer.concat([derivedKey.slice(16, 32), ciphertext]);
        const mac = crypto.createHash('sha3-256').update(validate).digest('hex');

        if (mac === targetMac) {
            console.log("\nMATCH FOUND!");
            console.log("PASSWORD: " + password);
            // Decrypt ciphertext to get private key
            const iv = Buffer.from(content.crypto.cipherparams.iv, 'hex');
            const decipher = crypto.createDecipheriv('aes-128-ctr', derivedKey.slice(0, 16), iv);
            const privateKey = Buffer.concat([decipher.update(ciphertext), decipher.final()]);
            console.log("PRIVATE_KEY: 0x" + privateKey.toString('hex'));
            process.exit(0);
        }
    } catch (e) {}
});
console.log("No matches found in candidate list.");
