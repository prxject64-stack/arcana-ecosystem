var fromAddress = "0x14a3256052c02f9d87fe1cc3b712d4530061b25c";
// Standard Identity Proxy Bytecode (Valid Even Length)
var identityBytecode = "0x6080604052348015600f57600080fd5b50603e80601d6000396000f3fe6080604052600080fdfea2646970667358221220790866037a1f287f35467475f411425e4063857319087c06c88681e808383a1a64736f6c63430008120033";

console.log("Deploying Identity Layer from: " + fromAddress);

var txHash = eth.sendTransaction({
    from: fromAddress,
    data: identityBytecode,
    gas: 3000000
});

console.log("Transaction Sent! Hash: " + txHash);

// Wait a moment for the miner to pick it up
admin.sleep(2);
var receipt = eth.getTransactionReceipt(txHash);
if (receipt && receipt.contractAddress) {
    console.log("IDENTITY LAYER DEPLOYED AT: " + receipt.contractAddress);
} else {
    console.log("Waiting for block confirmation... Check eth.getTransactionReceipt('" + txHash + "') in a moment.");
}
