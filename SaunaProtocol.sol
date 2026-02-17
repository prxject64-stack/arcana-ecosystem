// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
interface IArcanaCC {
    function transferWithSweat(address to, uint256 amount, uint256 load) external returns (bool);
}
contract SaunaProtocol {
    address public ccToken;
    constructor(address _ccToken) { ccToken = _ccToken; }
    function deposit(uint256 amount) external { }
}
