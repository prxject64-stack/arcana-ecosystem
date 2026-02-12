// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import "forge-std/Script.sol";
import "src/ArcanaBridgeL1.sol";

contract DeployArcana is Script {
    function run() external {
        // The Checksummed CC Token Address
        address ccToken = 0xBdae565eff11d46dfD2154442f0a565B4011F3b8;

        // Retrieve private key from environment or use a placeholder for now
        uint256 deployerPrivateKey = vm.envUint("PRIVATE_KEY");

        vm.startBroadcast(deployerPrivateKey);

        // Deploying the verified Bridge
        ArcanaBridgeL1 bridge = new ArcanaBridgeL1(ccToken);

        vm.stopBroadcast();
    }
}
