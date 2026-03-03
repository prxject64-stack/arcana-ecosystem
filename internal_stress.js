var sender = eth.accounts[0];
var amount = web3.toWei(1, "ether"); 
var totalSwaps = 4500;
var target = "0x0000000000000000000000000000000000000000";

// Fetch the starting nonce once to prevent "Already Known" errors
var currentNonce = eth.getTransactionCount(sender);

console.log("Starting 4,500 Sequential Swaps from Nonce: " + currentNonce);

for (var i = 0; i < totalSwaps; i++) {
    eth.sendTransaction({
        from: sender,
        to: target,
        value: amount,
        gas: 21000,
        gasPrice: 1000000000, // 1 Gwei
        nonce: currentNonce + i // Explicitly set the nonce
    });
    if (i % 500 === 0) {
        console.log("Queued " + i + " transactions...");
    }
}
console.log("Injection Complete. Run txpool.status to verify 4,500 pending.");
