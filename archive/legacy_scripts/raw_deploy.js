var owner = "0x14A3256052C02f9d87fE1cC3b712d4530061b25c";
var ccAddr = "39038Ab99d2E2445E336684507d8C392DA41A4bb"; // No 0x
var amount = "0000000000000000000000000000000000000000000000056bc75e2d63100000"; // 100 CC in Hex

// Load your BIN (Make sure this path is correct or paste the hex directly)
var bin = "PASTE_YOUR_FULL_BIN_HERE"; 

// Construct Data: [Bytecode] + [Padding + CC Address] + [100 CC Hex]
var encodedCC = "000000000000000000000000" + ccAddr;
var fullData = "0x" + bin + encodedCC + amount;

console.log("Initiating Raw Deployment...");
var tx = eth.sendTransaction({
    from: owner,
    data: fullData,
    gas: 4000000
});

console.log("Deployment TX Hash: " + tx);
while(eth.getTransactionReceipt(tx) == null) { admin.sleep(1); }
var newAddr = eth.getTransactionReceipt(tx).contractAddress;
console.log("\n--- DEPLOYMENT SUCCESS ---");
console.log("NEW_PASSPORT_ADDRESS: " + newAddr);
console.log("--------------------------");
