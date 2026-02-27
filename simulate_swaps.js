var count = 4500;
var vault = "0xe7B7B6cC21D01e6120197f0413d224923243B69c";
var destination = "0x000000000000000000000000000000000000dead"; // Burn address for testing

console.log("Commencing " + count + " simultaneous CC-P swaps...");

for (var i = 0; i < count; i++) {
    eth.sendTransaction({
        from: vault,
        to: destination,
        value: web3.toWei(0.001, "ether"), // Swap increments
        gas: 21000,
        nonce: eth.getTransactionCount(vault) + i
    });
}
console.log("Swaps Broadcasted to Xeon Transaction Pool.");
