var owner = "0x14A3256052C02f9d87fE1cC3b712d4530061b25c";
var ccAddr = "0x39038Ab99d2E2445E336684507d8C392DA41A4bb";
var passAddr = "0x715cb0edcf88de9f3b1641a40a24ab3d7793dbe0";

// Replace with your actual second test wallet address
var peerAddr = "0xPASTE_YOUR_SECOND_WALLET_ADDRESS_HERE"; 

var ccAbi = [{"constant": false, "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "transfer", "outputs": [{"name": "success", "type": "bool"}], "type": "function"}];
var passAbi = [{"inputs": [], "name": "performSacrifice", "outputs": [], "stateMutability": "nonpayable", "type": "function"}];

try {
    var cc = eth.contract(ccAbi).at(ccAddr);
    var passport = eth.contract(passAbi).at(passAddr);

    console.log("1. Sending 100 CC to Peer for Naturalization...");
    var tx1 = cc.transfer(peerAddr, web3.toWei(100, "ether"), {from: owner});
    while(eth.getTransactionReceipt(tx1) == null) { admin.sleep(1); }
    
    console.log("2. Sending ETH for Gas...");
    var tx2 = eth.sendTransaction({from: owner, to: peerAddr, value: web3.toWei(0.1, "ether")});
    while(eth.getTransactionReceipt(tx2) == null) { admin.sleep(1); }

    console.log("\n--- PEER READY FOR NATURALIZATION ---");
    console.log("Peer now has the 100 CC and Gas required to call performSacrifice().");
} catch (e) {
    console.log("ERROR: " + e.message);
}
