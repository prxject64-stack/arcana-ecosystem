var passAddr = "0x7F658eB0fd198929267Bf02a54bbafA6304255E8";
console.log("\n--- RAW STORAGE DUMP ---");
for (var i = 0; i < 5; i++) {
    var val = eth.getStorageAt(passAddr, i);
    console.log("Slot " + i + ": " + val);
}

var code = eth.getCode(passAddr);
console.log("\n--- CODE METRICS ---");
console.log("Bytecode Length: " + code.length + " characters");
if (code.length <= 2) {
    console.log("CRITICAL: No code found at this address!");
}
