var owner = "0x14A3256052C02f9d87fE1cC3b712d4530061b25c";
var ccAddr = "0x39038Ab99d2E2445E336684507d8C392DA41A4bb";
var passAddr = "0x715cb0edcf88de9f3b1641a40a24ab3d7793dbe0";

// PASTE THE NEW ADDRESS PRODUCED BY GETH HERE
var peerAddr = "0x_PASTE_NEW_ADDRESS_HERE_"; 

var ccAbi = [{"constant": false, "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "transfer", "outputs": [{"name": "success", "type": "bool"}], "type": "function"}];

try {
    var cc = eth.contract(ccAbi).at(ccAddr);

    console.log("Transferring 0.5 ETH for Gas...");
    eth.sendTransaction({from: owner, to: peerAddr, value: web3.toWei(0.5, "ether")});

    console.log("Transferring 100 CC for Naturalization...");
    var tx = cc.transfer(peerAddr, web3.toWei(100, "ether"), {from: owner});
    
    while(eth.getTransactionReceipt(tx) == null) { admin.sleep(1); }
    console.log("Peer Funded Successfully. TX: " + tx);
} catch (e) {
    console.log("ERROR: " + e.message);
}
