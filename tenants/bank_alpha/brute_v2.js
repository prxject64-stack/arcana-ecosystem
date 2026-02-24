const crypto = require('crypto');
const fs = require('fs');
const path = "/root/arcana-ecosystem/arcana_data/keystore/UTC--2026-02-24T03-24-11.552875466Z--c4bbb118acc45f1be50de724f1757b1a19e19de3";
const content = JSON.parse(fs.readFileSync(path, 'utf8'));
const kdfparams = content.crypto.kdfparams;
const salt = Buffer.from(kdfparams.salt, 'hex');
const ciphertext = Buffer.from(content.crypto.ciphertext, 'hex');
const targetMac = content.crypto.mac;

// Expanded candidates based on node history patterns
const candidates = [
    "arcana", "Arcana", "sauna", "Sauna",
    "arcana2026", "Arcana2026!", "Deezydeezydeezy1$",
    "password", "Password", "123456", " ", "\n", "",
    "YOUR_SAVED_PASSWORD", "YOUR_SAVED_PASSWORD\n"
];

candidates.forEach(pw => {
    const derivedKey = crypto.scryptSync(pw, salt, kdfparams.dklen, {
        N: kdfparams.n, r: kdfparams.r, p: kdfparams.p, maxmem: 1024 * 1024 * 1024
    });
    const validate = Buffer.concat([derivedKey.slice(16, 32), ciphertext]);
    const mac = crypto.createHash('sha3-256').update(validate).digest('hex');
    if (mac === targetMac) {
        console.log(`\nMATCH FOUND: "${pw}"`);
        const iv = Buffer.from(content.crypto.cipherparams.iv, 'hex');
        const decipher = crypto.createDecipheriv('aes-128-ctr', derivedKey.slice(0, 16), iv);
        const pk = Buffer.concat([decipher.update(ciphertext), decipher.final()]);
        console.log(`PRIVATE_KEY: 0x${pk.hex()}`);
        process.exit(0);
    }
});
console.log("No match.");
