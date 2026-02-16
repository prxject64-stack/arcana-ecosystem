var passAddr = "0x7F658eB0fd198929267Bf02a54bbafA6304255E8";
var owner = "0x14A3256052C02f9d87fE1cC3b712d4530061b25c";

// Checking if an update function exists in your logic
var abi = [{"inputs": [{"name": "_amount", "type": "uint256"}], "name": "setSacrificeAmount", "outputs": [], "stateMutability": "nonpayable", "type": "function"}];

try {
    var passport = eth.contract(abi).at(passAddr);
    var amount = web3.toWei(100, "ether");
    console.log("Attempting to set sacrificeAmount to 100 CC...");
    var tx = passport.setSacrificeAmount(amount, {from: owner, gas: 500000});
    console.log("Update TX: " + tx);
    while(eth.getTransactionReceipt(tx) == null) { admin.sleep(1); }
    console.log("Update MINED. Slot 1 should now be 0x56bc75e2d63100000...");
} catch (e) {
    console.log("Update Failed: " + e.message + ". We may need to redeploy the Passport with a constructor value.");
}
