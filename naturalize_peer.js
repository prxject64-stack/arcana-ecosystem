var peer = "0x4F9595e22A0881B1a13F9AC039B45a3Eb56D6497";
var passAddr = "0x715cb0edcf88de9f3b1641a40a24ab3d7793dbe0";
var ccAddr = "0x39038Ab99d2E2445E336684507d8C392DA41A4bb";
var passAbi = [{"inputs": [], "name": "performSacrifice", "outputs": [], "stateMutability": "nonpayable", "type": "function"}];
var ccAbi = [{"constant": false, "inputs": [{"name": "_spender", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "approve", "outputs": [{"name": "success", "type": "bool"}], "type": "function"}];

try {
    console.log("Unlocking Peer Account 0x4F95...");
    // Using the password provided to resolve the lock
    personal.unlockAccount(peer, "Deezydeezydeezy1$", 300); 

    var passport = eth.contract(passAbi).at(passAddr);
    var cc = eth.contract(ccAbi).at(ccAddr);

    console.log("Peer: Approving 100 CC...");
    var appTx = cc.approve(passAddr, web3.toWei(100, "ether"), {from: peer, gas: 500000});
    while(eth.getTransactionReceipt(appTx) == null) { admin.sleep(1); }

    console.log("Peer: Executing Sacrifice...");
    var sacTx = passport.performSacrifice({from: peer, gas: 1000000});
    while(eth.getTransactionReceipt(sacTx) == null) { admin.sleep(1); }

    if (eth.getTransactionReceipt(sacTx).status == "0x1") {
        console.log("\n--- PEER #1 STATUS: ACTIVE ---");
        console.log("Sovereign Network size: 2 Citizens.");
    } else {
        console.log("REVERTED. Check if 100 CC was actually transferred to Peer.");
    }
} catch (e) {
    console.log("ERROR: " + e.message);
}
