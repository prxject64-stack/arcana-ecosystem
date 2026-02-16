var abi = [{"inputs":[{"internalType":"address","name":"_ccTokenAddress","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"citizen","type":"address"},{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"Naturalized","type":"event"},{"inputs":[],"name":"BURN_ADDRESS","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"SACRIFICE_AMOUNT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"ccToken","outputs":[{"internalType":"contract ICCPrivate","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"isCitizen","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"performSacrifice","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"totalCitizens","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}];
var addr = "0xe7df03eb083a4ea5b84d25ceb6f187a1b0651cdd";
var contract = eth.contract(abi).at(addr);

console.log("\n--- ARCANA PASSPORT DEEP SCAN ---");
try {
    var sacrifice = contract.SACRIFICE_AMOUNT();
    console.log("FUNCTION CALL SUCCESS!");
    console.log("Sacrifice Amount: " + (sacrifice / 1e18) + " CC");
    console.log("Total Citizens:   " + contract.totalCitizens());
} catch (e) {
    console.log("FUNCTION CALL FAILED: " + e);
    console.log("Bytecode length: " + eth.getCode(addr).length);
}
console.log("---------------------------------");
