// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CreditCoinPrivate {
    mapping(address => uint256) public balanceOf;
    uint256 public totalSupply = 136000000000 * 10**18;

    constructor() {
        balanceOf[msg.sender] = totalSupply;
    }

    function transfer(address to, uint256 val) public returns (bool) {
        require(balanceOf[msg.sender] >= val);
        balanceOf[msg.sender] -= val;
        balanceOf[to] += val;
        return true;
    }
}