var passAddr = "0x7F658eB0fd198929267Bf02a54bbafA6304255E8";
var owner = "0x14A3256052C02f9d87fE1cC3b712d4530061b25c";
var data = "0x368b8772"; // The function selector for performSacrifice()

console.log("\n--- SIMULATING REVERT ---");
try {
    var result = eth.call({from: owner, to: passAddr, data: data});
    console.log("Raw Result: " + result);
} catch (e) {
    console.log("REVERT REASON: " + e.message);
}
