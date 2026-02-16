var bin = "0x" + cat("contracts/build/CCPrivate.full.bin");
var abi = JSON.parse(cat("contracts/build/CCPrivate.abi"));

console.log("Deploying Credit Coin Private (CC)...");

var txHash = eth.sendTransaction({
    from: eth.accounts[0],
    data: bin,
    gas: 5000000,
    gasPrice: eth.gasPrice
});

while (true) {
    var receipt = eth.getTransactionReceipt(txHash);
    if (receipt && receipt.contractAddress) {
        console.log("\n--- CC TOKEN LIVE ---");
        console.log("Address: " + receipt.contractAddress);
        console.log("Size:    " + eth.getCode(receipt.contractAddress).length + " bytes");
        break;
    }
    admin.sleep(1);
}
