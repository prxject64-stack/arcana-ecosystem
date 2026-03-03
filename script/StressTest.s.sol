// SPDX-License-Identifier: MIT
pragma solidity 0.8.28;

import "forge-std/Script.sol";
import "../src/SaunaVault.sol";

contract StressTest is Script {
    function run(address saUSDAddress, address vaultAddress) external {
        uint256 pk = vm.envUint("PRIVATE_KEY");
        vm.startBroadcast(pk);
        
        // Simulating the 4,500 swap blast logic
        // For testing connectivity, we do a simple static call or minor tx
        SaunaVault(vaultAddress).deposit(0); 
        
        vm.stopBroadcast();
    }
}
