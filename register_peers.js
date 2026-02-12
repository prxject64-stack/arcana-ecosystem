var identityAddr = "0x73da448eccae7b5fa064f8d39cb97396e445fcc3";
var fromAddr = "0x5D815B693A80DED53fc19A9d8892B822895Ee6dD";
var totalPeers = 100; // Starting with a test batch of 100

console.log("Registering " + totalPeers + " peers to Identity Layer...");

for (var i = 0; i < totalPeers; i++) {
    // Generate a pseudo-deterministic peer address for the ecosystem
    var peerAddr = "0x" + web3.sha3(i.toString()).substring(26);
    
    eth.sendTransaction({
        from: fromAddr,
        to: identityAddr,
        data: "0x4420e486" + peerAddr.substring(2), // Example function selector: register(address)
        gas: 100000
    });
}
console.log("Batch 1 submitted. Check eth.pendingTransactions.");
