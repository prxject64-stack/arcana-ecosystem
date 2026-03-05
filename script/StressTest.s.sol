// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;
import "forge-std/Script.sol";

contract StressTest is Script {
    function run() external {
        address amm = vm.envAddress("AMM_V2");
        address deployer = 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266;
        
        // Use the specific unlocked address for the broadcast
        vm.startBroadcast(deployer);
        
        for (uint i = 0; i < 4500; i++) {
            // Raw call to the swap function: 0xf959f8c3
            (bool success, ) = amm.call(abi.encodeWithSelector(0xf959f8c3, 1 ether));
            if (!success) {
                // If one fails, we need to know why. 
                // Using console.log will slow it down but provide the raw data.
                revert("Swap failed at iteration");
            }
        }
        vm.stopBroadcast();
    }
}
