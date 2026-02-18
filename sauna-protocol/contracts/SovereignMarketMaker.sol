// SPDX-License-Identifier: MIT
pragma solidity ^0.8.33;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SovereignMarketMaker is Ownable {
    IERC20 public sUSD;
    IERC20 public CC;
    
    // 1 sUSD = 100 CC ($0.01 peg)
    uint256 public constant EXCHANGE_RATE = 100;

    constructor(address _sUSD, address _CC) Ownable(msg.sender) {
        sUSD = IERC20(_sUSD);
        CC = IERC20(_CC);
    }

    // User sells sUSD to the Treasury for CC
    function sellSUSD(uint256 sUSDAmount) external {
        uint256 ccAmount = sUSDAmount * EXCHANGE_RATE;
        require(CC.balanceOf(address(this)) >= ccAmount, "Treasury: Out of CC");
        
        require(sUSD.transferFrom(msg.sender, address(this), sUSDAmount), "Transfer failed");
        require(CC.transfer(msg.sender, ccAmount), "Payout failed");
    }

    // User buys sUSD from the Treasury using CC
    function buySUSD(uint256 ccAmount) external {
        uint256 sUSDAmount = ccAmount / EXCHANGE_RATE;
        require(sUSD.balanceOf(address(this)) >= sUSDAmount, "Treasury: Out of sUSD");
        
        require(CC.transferFrom(msg.sender, address(this), ccAmount), "Transfer failed");
        require(sUSD.transfer(msg.sender, sUSDAmount), "Payout failed");
    }

    function withdrawReserves(address token) external onlyOwner {
        IERC20(token).transfer(owner(), IERC20(token).balanceOf(address(this)));
    }
}
