// SPDX-License-Identifier: MIT
pragma solidity 0.8.28;

import "forge-std/Script.sol";
import "../src/SaunaVault.sol";

contract DeploySauna is Script {
    function run() external {
        uint256 deployerPrivateKey = vm.envUint("PRIVATE_KEY");
        address deployerAddress = vm.addr(deployerPrivateKey);

        vm.startBroadcast(deployerPrivateKey);

        // Replace with your actual saUSD token address
        address saUSDAddress = 0x71C7656EC7ab88b098defB751B7401B5f6d8976F; 

        // Deploying SaunaVault with EXACTLY 2 arguments: (token, initialOwner)
        new SaunaVault(
            saUSDAddress,
            deployerAddress
        );

        vm.stopBroadcast();
    }
}
