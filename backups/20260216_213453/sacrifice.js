var ccAddr = "0x39038Ab99d2E2445E336684507d8C392DA41A4bb";
var passAddr = "0x7F658eB0fd198929267Bf02a54bbafA6304255E8";
var owner = "0x14A3256052C02f9d87fE1cC3b712d4530061b25c";

var passAbi = [{"inputs": [], "name": "performSacrifice", "outputs": [], "stateMutability": "nonpayable", "type": "function"}];

try {
    var passport = eth.contract(passAbi).at(passAddr);
    console.log("Initiating Sacrifice from " + owner);
    
    // We already approved the 100 CC in a previous step, so this should work.
    var tx = passport.performSacrifice({from: owner, gas: 1000000});
    console.log("Sacrifice TX: " + tx);
    
    console.log("Waiting for mining...");
    while(eth.getTransactionReceipt(tx) == null) { admin.sleep(1); }
    console.log("Sacrifice MINED.");
} catch (e) {
    console.log("FATAL ERROR: " + e.message);
}
