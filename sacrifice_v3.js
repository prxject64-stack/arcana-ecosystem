var passAddr = "0x7F658eB0fd198929267Bf02a54bbafA6304255E8";
var owner = "0x14A3256052C02f9d87fE1cC3b712d4530061b25c";
var passAbi = [{"inputs": [], "name": "performSacrifice", "outputs": [], "stateMutability": "nonpayable", "type": "function"}];

try {
    var passport = eth.contract(passAbi).at(passAddr);
    console.log("DEBUG: Attempting Sacrifice with 4M Gas Limit...");
    
    // Using high gas to ensure it's not a gas exhaustion issue
    var tx = passport.performSacrifice({from: owner, gas: 4000000});
    console.log("TX Hash: " + tx);

    while(eth.getTransactionReceipt(tx) == null) { admin.sleep(1); }
    
    var receipt = eth.getTransactionReceipt(tx);
    if (receipt.status == "0x1" || receipt.status == 1) {
        console.log("SUCCESS: Citizen #1 Naturalized.");
    } else {
        console.log("REVERTED: TX failed with status 0x0.");
        console.log("Check if the Passport contract is paused or if the balance is locked.");
    }
} catch (e) {
    console.log("SCRIPT ERROR: " + e.message);
}
