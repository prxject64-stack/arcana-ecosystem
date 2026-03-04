// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import "forge-std/Script.sol";
import "../src/ArcanaAMM.sol";

contract DeployTriadAMM is Script {
    function run() external {
        address saUSD = 0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512;
        address ccP = 0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512;
        address arcS = 0x5FbDB2315678afecb367f032d93F642f64180aa3;

        vm.startBroadcast();
        new ArcanaAMM(saUSD, ccP, arcS);
        vm.stopBroadcast();
    }
}