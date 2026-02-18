// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.33;

contract SaunaSecurity {
    address public sovereign;
    mapping(address => bool) public authorizedNodes;

    constructor() { sovereign = msg.sender; }

    modifier onlySovereign() {
        require(msg.sender == sovereign, "Sauna: Unauthorized Access");
        _;
    }

    function authorizeNode(address node) external onlySovereign {
        authorizedNodes[node] = true;
    }

    function checkLiquidityAccess(address user) external view returns (bool) {
        return authorizedNodes[user];
    }
}
