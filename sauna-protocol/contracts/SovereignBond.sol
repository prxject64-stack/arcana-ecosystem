// SPDX-License-Identifier: MIT
pragma solidity ^0.8.33;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract SovereignBond {
    IERC20 public sUSD;
    IERC20 public CC;
    
    mapping(address => uint256) public stakedBalance;
    uint256 public rewardRate = 10; // 10% CC reward for every sUSD staked (simulation)

    constructor(address _sUSD, address _CC) {
        sUSD = IERC20(_sUSD);
        CC = IERC20(_CC);
    }

    function stake(uint256 amount) external {
        require(sUSD.transferFrom(msg.sender, address(this), amount), "Stake failed");
        stakedBalance[msg.sender] += amount;
    }

    function claimRewards() external {
        uint256 reward = stakedBalance[msg.sender] * rewardRate / 100;
        require(CC.balanceOf(address(this)) >= reward, "Bonding Reserve Empty");
        CC.transfer(msg.sender, reward);
    }
}
