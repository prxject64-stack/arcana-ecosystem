var sender = eth.coinbase;
var receiver = "0xC773179F184BA9a895B5e5C85aa5D1a5Ea3556b0";
var password = "Deezydeezydeezy1$";
personal.unlockAccount(sender, password, 3600);

var nextNonce = eth.getTransactionCount(sender, "pending");
console.log("Starting broadcast from nonce: " + nextNonce);

for (var i = 0; i < 4500; i++) {
    eth.sendTransaction({
        from: sender,
        to: receiver,
        value: web3.toWei(0.1, "ether"),
        gasPrice: "1000000000",
        nonce: nextNonce + i
    });
    if (i % 500 === 0) { console.log("Injected " + i + " swaps..."); }
}
console.log("Verify now with txpool.status");
