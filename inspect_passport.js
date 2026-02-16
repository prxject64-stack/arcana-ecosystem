var ccAddr = "0x39038Ab99d2E2445E336684507d8C392DA41A4bb";
var passAddr = "0x7F658eB0fd198929267Bf02a54bbafA6304255E8";
var owner = "0x14A3256052C02f9d87fE1cC3b712d4530061b25c";

var passAbi = [
    {"inputs": [], "name": "ccToken", "outputs": [{"type": "address"}], "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "sacrificeAmount", "outputs": [{"type": "uint256"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"name": "", "type": "address"}], "name": "isCitizen", "outputs": [{"name": "", "type": "bool"}], "stateMutability": "view", "type": "function"}
];

try {
    var passport = eth.contract(passAbi).at(passAddr);
    console.log("\n--- PASSPORT INTERNAL AUDIT ---");
    
    // Check if the Passport knows where the CC Token is
    var linkedCC = passport.ccToken.call();
    console.log("Linked CC Address: " + linkedCC);
    if (linkedCC.toLowerCase() !== ccAddr.toLowerCase()) {
        console.log("CRITICAL ERROR: Passport is looking for CC at " + linkedCC + " but your token is at " + ccAddr);
    }

    // Check the required amount
    var amount = passport.sacrificeAmount.call();
    console.log("Required Sacrifice: " + (amount / 1e18) + " CC");

    // Check if you are already a citizen (unlikely, but check)
    var status = passport.isCitizen.call(owner);
    console.log("Current Status:     " + status);
    
} catch (e) {
    console.log("READ ERROR: " + e.message + " (This likely means these variables don't exist in your ABI/Contract)");
}
