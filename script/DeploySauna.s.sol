// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import "forge-std/Script.sol";
import "../src/SaunaVault.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract DeploySauna is Script {
    function run() external {
        address sausd = vm.envAddress("SAUSD_ADDR");
        vm.startBroadcast();
        new SaunaVault(IERC20(sausd));
        vm.stopBroadcast();
    }
}
