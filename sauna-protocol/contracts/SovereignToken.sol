// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract SovereignToken {
    mapping(address => uint256) public balanceOf;
    string public name;
    string public symbol;
    uint8 public decimals = 18;
    uint256 public totalSupply = 146000000000 * 10**18;

    constructor(string memory _name, string memory _symbol) {
        name = _name;
        symbol = _symbol;
    }

    function transfer(address to, uint256 amount) public returns (bool) {
        require(balanceOf[msg.sender] >= amount, "Sovereign: Insufficient funds");
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
        return true;
    }
}
