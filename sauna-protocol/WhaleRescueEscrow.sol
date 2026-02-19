// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract WhaleRescueEscrow {
    address public Jones; // Damarieus Jones
    
    struct Swap {
        address whale;
        uint256 sUSDAmount;
        uint256 ARCAmount;
        bool completed;
    }

    mapping(uint256 => Swap) public swaps;

    constructor() {
        Jones = msg.sender;
    }

    function initiateRescue(uint256 id, address whale, uint256 sUSD, uint256 arc) external {
        require(msg.sender == Jones, "Unauthorized");
        swaps[id] = Swap(whale, sUSD, arc, false);
    }

    function executeSwap(uint256 id) external {
        Swap storage s = swaps[id];
        require(msg.sender == s.whale, "Only the Whale can trigger");
        
        // Trustless Transfer
        IERC20(0xARC).transferFrom(Jones, s.whale, s.ARCAmount);
        IERC20(0xSUSD).transferFrom(s.whale, Jones, s.sUSDAmount);
        
        s.completed = true;
    }
}
