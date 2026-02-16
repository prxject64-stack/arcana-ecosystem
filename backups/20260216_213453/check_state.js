var abi = JSON.parse('[{"inputs":[{"internalType":"address","name":"_ccTokenAddress","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"citizen","type":"address"},{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"Naturalized","type":"event"},{"inputs":[],"name":"BURN_ADDRESS","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"SACRIFICE_AMOUNT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"ccToken","outputs":[{"internalType":"contract ICCPrivate","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"isCitizen","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"performSacrifice","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"totalCitizens","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]');
var addr = "0x48adc89754286c504cb1b47453647cac91486044";
var contract = eth.contract(abi).at(addr);

console.log("\n--- ARCANA SOVEREIGN PASSPORT ---");
console.log("Contract Address: " + addr);

try {
    var total = contract.totalCitizens();
    var sacrifice = contract.SACRIFICE_AMOUNT();
    console.log("Total Citizens:   " + total);
    console.log("Sacrifice Amount: " + (sacrifice / 1e18) + " CC");
} catch (e) {
    console.log("ERROR calling functions: " + e);
}
console.log("---------------------------------");
