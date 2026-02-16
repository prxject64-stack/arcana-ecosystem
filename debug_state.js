var txHash = "0x67fd4c2348b60dc9316714448d38bb1096b8480ceec2065381ee3c9dbf41421b";
var receipt = eth.getTransactionReceipt(txHash);

console.log("\n--- TRANSACTION DEBUG ---");
if (receipt) {
    console.log("TX Status:   " + receipt.status + " (0x0 = Fail, 0x1 = Success)");
    console.log("Gas Used:    " + receipt.gasUsed);
} else {
    console.log("TX Not Found. It may have been dropped from the pool.");
}

var ccAddr = "0x39038Ab99d2E2445E336684507d8C392DA41A4bb";
var passAddr = "0x7F658eB0fd198929267Bf02a54bbafA6304255E8";
var owner = "0x14A3256052C02f9d87fE1cC3b712d4530061b25c";
var abi = [{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"type":"function"}];

var cc = eth.contract(abi).at(ccAddr);
var remaining = cc.allowance(owner, passAddr);
console.log("Allowance:   " + (remaining / 1e18) + " CC");
console.log("-------------------------\n");
