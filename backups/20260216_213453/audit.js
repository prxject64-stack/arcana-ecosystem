var ccAddr = "0x39038Ab99d2E2445E336684507d8C392DA41A4bb";
var passAddr = "0x7F658eB0fd198929267Bf02a54bbafA6304255E8";
var owner = "0x14A3256052C02f9d87fE1cC3b712d4530061b25c"; 

var abi = [{"constant": true, "inputs": [{"name": "_owner", "type": "address"}], "name": "balanceOf", "outputs": [{"name": "balance", "type": "uint256"}], "type": "function"}];
var passAbi = [{"inputs": [{"name": "", "type": "address"}], "name": "isCitizen", "outputs": [{"name": "", "type": "bool"}], "stateMutability": "view", "type": "function"}];

try {
    var cc = eth.contract(abi).at(ccAddr);
    var passport = eth.contract(passAbi).at(passAddr);

    console.log("Querying Arcanum Ledger (Local Call)...");
    
    // Explicitly use .call() to avoid the transaction formatter
    var balance = cc.balanceOf.call(owner);
    var citizen = passport.isCitizen.call(owner);

    console.log("\n--- ARCANUM MASTER AUDIT ---");
    console.log("Sovereign:      " + owner);
    console.log("CC Balance:     " + (balance / 1e18) + " CC");
    console.log("Citizen Status: " + citizen);
    console.log("----------------------------");

} catch (e) {
    console.log("FATAL ERROR: " + e.message);
}
