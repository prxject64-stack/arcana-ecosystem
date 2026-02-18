// SPDX-License-Identifier: MIT
pragma solidity ^0.8.33;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SaunaProtocol is Ownable {
    mapping(address => mapping(address => uint256)) public rates;

    event RateUpdated(address base, address quote, uint256 rate);
    event SwapExecuted(address indexed user, address indexed fromToken, address indexed toToken, uint256 amountIn, uint256 amountOut);

    constructor() Ownable(msg.sender) {}

    function setExchangeRate(address base, address quote, uint256 rate) external onlyOwner {
        rates[base][quote] = rate;
        emit RateUpdated(base, quote, rate);
    }

    function swap(address fromToken, address toToken, uint256 amountIn) external {
        uint256 rate = rates[fromToken][toToken];
        require(rate > 0, "Sauna: Pair not supported");
        
        uint256 amountOut = amountIn / rate;

        // CRITICAL FIX: Ensure the CC is actually taken from the user
        bool success = IERC20(fromToken).transferFrom(msg.sender, address(this), amountIn);
        require(success, "Sauna: Transfer failed - check allowance");
        
        // Ensure the Vault has enough sUSD to pay out
        require(IERC20(toToken).balanceOf(address(this)) >= amountOut, "Sauna: Insufficient liquidity");
        
        IERC20(toToken).transfer(msg.sender, amountOut);

        emit SwapExecuted(msg.sender, fromToken, toToken, amountIn, amountOut);
    }
}
