var peer = "0x4F9595e22A0881B1a13F9AC039B45a3Eb56D6497";
var pass = "Deezydeezydeezy1$";
var passAddr = "0x715cb0edcf88de9f3b1641a40a24ab3d7793dbe0";
var ccAddr = "0x39038Ab99d2E2445E336684507d8C392DA41A4bb";

var passAbi = [{"inputs": [], "name": "performSacrifice", "outputs": [], "stateMutability": "nonpayable", "type": "function"}];
var ccAbi = [{"constant": false, "inputs": [{"name": "_spender", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "approve", "outputs": [{"name": "success", "type": "bool"}], "type": "function"}];

var passport = eth.contract(passAbi).at(passAddr);
var cc = eth.contract(ccAbi).at(ccAddr);

// Force sending without global unlock
try {
    console.log("Attempting Direct Approval via Signed Transaction...");
    // Some Geth versions allow the password as the last argument in sendTransaction
    var tx1 = cc.approve.sendTransaction(passAddr, web3.toWei(100, "ether"), {from: peer, gas: 500000}, pass);
    console.log("Approve TX: " + tx1);
    
    while(eth.getTransactionReceipt(tx1) == null) { admin.sleep(1); }
    
    var tx2 = passport.performSacrifice.sendTransaction({from: peer, gas: 1000000}, pass);
    console.log("Sacrifice TX: " + tx2);
} catch (e) {
    console.log("CRITICAL ERROR: " + e.message);
    console.log("Geth security is blocking internal signing. We must use a Raw Signer.");
}
