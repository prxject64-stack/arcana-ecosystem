// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract SaunaProtocol {
    uint256 public constant MAX_SWAPS = 4500;
    uint256 public minBurn = 10;  // 0.1%
    uint256 public maxBurn = 100; // 1.0%
    address public constant DEAD = 0x000000000000000000000000000000000000dEaD;

    function calculateSweat(uint256 _amount, uint256 _currentSwaps) public view returns (uint256) {
        uint256 currentRate = minBurn;
        if (_currentSwaps > 0) {
            uint256 scale = (_currentSwaps * (maxBurn - minBurn)) / MAX_SWAPS;
            currentRate += scale;
        }
        if (currentRate > maxBurn) currentRate = maxBurn;
        return (_amount * currentRate) / 10000;
    }
}
