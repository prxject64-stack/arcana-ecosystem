pragma solidity ^0.8.20;
import "forge-std/Script.sol";
import "../src/ArcanaVault.sol";

contract DeployVault is Script {
    function run() external {
        address arcS = 0x5FbDB2315678afecb367f032d93F642f64180aa3;
        address saUSD = 0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512;
        vm.startBroadcast();
        new ArcanaVault(arcS, saUSD);
        vm.stopBroadcast();
    }
}