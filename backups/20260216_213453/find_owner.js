var passAddr = "0x7F658eB0fd198929267Bf02a54bbafA6304255E8";
console.log("\n--- IDENTITY PROBING ---");
for (var i = 0; i < 10; i++) {
    var val = eth.getStorageAt(passAddr, i);
    console.log("Slot " + i + ": " + val);
}
console.log("\nTarget Address: 0x00000000000000000000000014a3256052c02f9d87fe1cc3b712d4530061b25c");
