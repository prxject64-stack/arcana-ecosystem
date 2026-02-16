var owner = "0x14A3256052C02f9d87fE1cC3b712d4530061b25c";
var ccAddr = "0x39038Ab99d2E2445E336684507d8C392DA41A4bb";
var sacrificeAmount = web3.toWei(100, "ether");

// Full ABI for the new Passport
var abi = [{"inputs":[{"name":"_ccToken","type":"address"},{"name":"_amount","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"performSacrifice","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"","type":"address"}],"name":"isCitizen","outputs":[{"name":"","type":"bool"}],"stateMutability":"view","type":"function"}];

// Replace with your actual compiled bytecode from solc
var bin = "0x" + "PASTE_YOUR_ARCANAPASSPORT_BIN_HERE"; 

console.log("Deploying New Passport...");
var passportContract = eth.contract(abi);
var deployTx = passportContract.new(ccAddr, sacrificeAmount, {
    from: owner,
    data: bin,
    gas: 3000000
});

console.log("Deployment TX: " + deployTx);
while(eth.getTransactionReceipt(deployTx) == null) { admin.sleep(1); }
var newAddr = eth.getTransactionReceipt(deployTx).contractAddress;
console.log("NEW PASSPORT ADDRESS: " + newAddr);
