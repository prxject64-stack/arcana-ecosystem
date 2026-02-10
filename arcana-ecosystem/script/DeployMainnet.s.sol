// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "forge-std/Script.sol";
import "../src/CreditCoin.sol";
import "../src/ArbExecutor.sol";

contract DeployMainnet is Script {
    function run() external {
        uint256 deployerPrivateKey = vm.envUint("PRIVATE_KEY");
        
        vm.startBroadcast(deployerPrivateKey);

        // Deploying CC to Base Mainnet
        CreditCoin cc = new CreditCoin();
        
        // Deploying ArbExecutor
        ArbExecutor executor = new ArbExecutor();
        
        // Immediate Security Handshake
        // Promoting God-Key to Principal on Mainnet
        executor.setPrincipal(0x0Ed60278e8A7C9520611EBDcB214C374b91BF05e);

        vm.stopBroadcast();
    }
}
