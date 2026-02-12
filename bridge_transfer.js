var sender = "0xc6757efa426a3fc4ea842dc36c6658032de25d07";
var receiver = "0xc6757efa426a3fc4ea842dc36c6658032de25d07"; // Self-transfer to bridge or specify target
var amount = "0x1b7709034e6c4205b40000000"; // 136B CC in Hex

var tx = eth.sendTransaction({
    from: sender,
    to: receiver,
    value: amount,
    gas: 21000,
    gasPrice: 0
});

console.log("Transaction Hash: " + tx);
