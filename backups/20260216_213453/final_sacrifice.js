var passAddr = "0x7F658eB0fd198929267Bf02a54bbafA6304255E8";
var owner = "0x14A3256052C02f9d87fE1cC3b712d4530061b25c";
var passAbi = [{"inputs": [], "name": "performSacrifice", "outputs": [], "stateMutability": "nonpayable", "type": "function"}];

try {
    var passport = eth.contract(passAbi).at(passAddr);
    console.log("Executing Sovereign Sacrifice...");
    var tx = passport.performSacrifice({from: owner, gas: 2000000});
    console.log("TX Hash: " + tx);

    while(eth.getTransactionReceipt(tx) == null) { admin.sleep(1); }
    
    var receipt = eth.getTransactionReceipt(tx);
    if (receipt.status == "0x1" || receipt.status == 1) {
        console.log("\n--- SUCCESS: CITIZEN #1 NATURALIZED ---");
    } else {
        console.log("REVERTED: Status 0x0. Check Geth logs for 'Out of Gas' or internal logic errors.");
    }
} catch (e) {
    console.log("FATAL ERROR: " + e.message);
}
