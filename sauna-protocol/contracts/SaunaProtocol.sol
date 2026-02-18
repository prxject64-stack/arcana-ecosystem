// SPDX-License-Identifier: MIT
pragma solidity ^0.8.33;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract SaunaProtocol {
    address public ccToken;
    bool public systemPaused;
    uint256 public constant MAX_BATCH_SIZE = 5000;
    uint256 public totalVaultLiquidity;
    mapping(uint256 => uint256) public blockVolume;

    constructor(address _ccToken) {
        ccToken = _ccToken;
        totalVaultLiquidity = 136000000000 * 10**18; // Sync with 136B CC
    }

    function processMassSwaps(address[] calldata recipients, uint256 amount) external {
        require(!systemPaused, "SEC: System Paused");
        require(recipients.length <= MAX_BATCH_SIZE, "SEC: Batch too large");
        
        uint256 totalValue = recipients.length * amount;
        
        // FIX: Check CC Token balance, not ETH balance
        uint256 currentBalance = IERC20(ccToken).balanceOf(address(this));
        require(totalValue <= currentBalance, "SEC: Insufficient Liquidity");

        uint256 limit = (totalVaultLiquidity * 10) / 100;
        require(blockVolume[block.number] + totalValue <= limit, "SEC: Circuit Breaker Tripped");

        blockVolume[block.number] += totalValue;

        for (uint256 i = 0; i < recipients.length; i++) {
            require(IERC20(ccToken).transfer(recipients[i], amount), "SEC: Transfer Failed");
        }
    }
}
