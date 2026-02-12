// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import "forge-std/Script.sol";
import "./ARC_SaunaShield.sol";

contract DeploySauna is Script {
    function run() external {
        uint256 deployerPrivateKey = vm.envUint("PRIVATE_KEY");
        vm.startBroadcast(deployerPrivateKey);

        // Replace SECOND_ADDRESS with your ARC address
        new SaunaShield(
            0x85756b22efea5C5178823fE309db787b6f1Ab6f6, 
            YOUR_ARC_CONTRACT_ADDRESS_HERE
        );

        vm.stopBroadcast();
    }
}
