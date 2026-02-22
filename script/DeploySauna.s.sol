// SPDX-License-Identifier: MIT
pragma solidity 0.8.19;

import "forge-std/Script.sol";
import "../src/SaunaVault.sol";
import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract DeploySauna is Script {
    function run() external {
        uint256 deployerPrivateKey = vm.envUint("DEPLOYER_PK");
        vm.startBroadcast(deployerPrivateKey);

        new SaunaVault(
            IERC20(0x62Fa3432DBb3BbEEd0F4EDdF4D25E6e4cADf9383),
            "Sauna USD",
            "saUSD"
        );

        vm.stopBroadcast();
    }
}
