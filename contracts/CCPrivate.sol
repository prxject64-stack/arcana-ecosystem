 // SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract CCPrivate {
    string public name = "Credit Coin Private";
    string public symbol = "CC";
    uint8 public decimals = 18;
    uint256 public totalSupply = 136000000000 * 10**18;
    mapping(address => uint256) public balanceOf;
    constructor() { balanceOf[msg.sender] = totalSupply; }
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(balanceOf[msg.sender] >= _value);
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        return true;
    }
}