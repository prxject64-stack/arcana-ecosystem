// SPDX-License-Identifier: MIT
pragma solidity ^0.8.33;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract SovereignBond {
    IERC20 public sUSD;
    IERC20 public CC;
    
    struct StakeInfo {
        uint256 amount;
        uint256 depositTimestamp;
        uint256 lastClaimTimestamp;
    }

    mapping(address => StakeInfo) public stakes;
    uint256 public rewardRate = 10; 
    uint256 public lockDuration = 7 days;

    constructor(address _sUSD, address _CC) {
        sUSD = IERC20(_sUSD);
        CC = IERC20(_CC);
    }

    function stake(uint256 amount) external {
        require(sUSD.transferFrom(msg.sender, address(this), amount), "Stake failed");
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].depositTimestamp = block.timestamp;
        stakes[msg.sender].lastClaimTimestamp = block.timestamp;
    }

    function withdraw(uint256 amount) external {
        require(stakes[msg.sender].amount >= amount, "Insufficient staked balance");
        require(block.timestamp >= stakes[msg.sender].depositTimestamp + lockDuration, "Principal has not matured");
        
        stakes[msg.sender].amount -= amount;
        require(sUSD.transfer(msg.sender, amount), "Withdrawal transfer failed");
    }

    function claimRewards() external {
        require(block.timestamp >= stakes[msg.sender].lastClaimTimestamp + lockDuration, "Rewards not yet matured");
        uint256 reward = (stakes[msg.sender].amount * rewardRate) / 100;
        require(reward > 0, "No rewards to claim");
        require(CC.balanceOf(address(this)) >= reward, "Bonding Reserve Empty");
        
        stakes[msg.sender].lastClaimTimestamp = block.timestamp; // Only reset reward timer
        CC.transfer(msg.sender, reward);
    }
}
