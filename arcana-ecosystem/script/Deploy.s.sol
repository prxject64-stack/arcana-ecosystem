// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "forge-std/Script.sol";
import "../src/ArbExecutor.sol";
import "../src/CreditCoin.sol";

contract DeployScript is Script {
    function run() external {
        uint256 deployerPrivateKey = vm.envUint("PRIVATE_KEY");
        vm.startBroadcast(deployerPrivateKey);

        // 1. Deploy the Token (Credit Coin Private)
        CreditCoin cc = new CreditCoin(); 
        
        // 2. Deploy the Executor
        ArbExecutor executor = new ArbExecutor();

        vm.stopBroadcast();
    }
}
