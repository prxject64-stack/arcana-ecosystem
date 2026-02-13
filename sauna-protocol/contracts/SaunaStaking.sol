// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

contract SaunaStaking {
    string public constant name = "Sauna Staking Protocol";
    uint256 public constant TOTAL_CC_LIQUIDITY = 136000000000;
    
    mapping(address => uint256) public balances;

    function deposit(uint256 amount) external {
        balances[msg.sender] += amount;
    }
}
