var owner = "0x14A3256052C02f9d87fE1cC3b712d4530061b25c";
var ccAddr = "0x39038Ab99d2E2445E336684507d8C392DA41A4bb";
var passAddr = "0x715cb0edcf88de9f3b1641a40a24ab3d7793dbe0";

var ccAbi = [{"constant": false, "inputs": [{"name": "_spender", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "approve", "outputs": [{"name": "success", "type": "bool"}], "type": "function"}];
var passAbi = [{"inputs": [], "name": "performSacrifice", "outputs": [], "stateMutability": "nonpayable", "type": "function"}];

try {
    var cc = eth.contract(ccAbi).at(ccAddr);
    var passport = eth.contract(passAbi).at(passAddr);

    console.log("Step 1: Approving 100 CC for New Passport...");
    var appTx = cc.approve(passAddr, web3.toWei(100, "ether"), {from: owner, gas: 500000});
    while(eth.getTransactionReceipt(appTx) == null) { admin.sleep(1); }
    console.log("Approval Confirmed: " + appTx);

    console.log("Step 2: Executing Sacrifice...");
    var sacTx = passport.performSacrifice({from: owner, gas: 1000000});
    while(eth.getTransactionReceipt(sacTx) == null) { admin.sleep(1); }
    
    if (eth.getTransactionReceipt(sacTx).status == "0x1") {
        console.log("\n--- ARCANA SOVEREIGN STATUS: ACTIVE ---");
        console.log("You are now a Citizen of the Arcana Ecosystem.");
    } else {
        console.log("REVERTED. Status 0x0.");
    }
} catch (e) {
    console.log("ERROR: " + e.message);
}
