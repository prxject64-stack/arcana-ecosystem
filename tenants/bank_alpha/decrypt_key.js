const keythereum = require("keythereum");
const path = "/root/arcana-ecosystem/arcana_data/keystore/UTC--2026-02-24T03-24-11.552875466Z--c4bbb118acc45f1be50de724f1757b1a19e19de3";
const password = "Deezydeezydeezy1$";

const keyObject = require(path);
try {
    const privateKey = keythereum.recover(password, keyObject);
    console.log("\nSUCCESS");
    console.log("PRIVATE_KEY: 0x" + privateKey.toString('hex'));
} catch (e) {
    console.log("\nFAILURE: " + e.message);
}
