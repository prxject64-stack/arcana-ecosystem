var ccAbi = [
    {"type":"constructor","inputs":[],"stateMutability":"nonpayable"},
    {"type":"function","name":"SOVEREIGN_VAULT","inputs":[],"outputs":[{"name":"","type":"address","internalType":"address"}],"stateMutability":"view"},
    {"type":"function","name":"balanceOf","inputs":[{"name":"account","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},
    {"type":"function","name":"mintSovereignReward","inputs":[{"name":"to","type":"address","internalType":"address"},{"name":"amount","type":"uint256","internalType":"uint256"}],"outputs":[],"stateMutability":"nonpayable"},
    {"type":"function","name":"totalSupply","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},
    {"type":"function","name":"transfer","inputs":[{"name":"to","type":"address","internalType":"address"},{"name":"value","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"stateMutability":"nonpayable"}
];

// REPLACE '0x_DEPLOYED_ADDRESS' with the address you get after running the deploy command
var ccAddr = "0x_DEPLOYED_ADDRESS";
var CC_TOKEN = eth.contract(ccAbi).at(ccAddr);

console.log("Mission Control: CreditCoin Private Bridge established.");
