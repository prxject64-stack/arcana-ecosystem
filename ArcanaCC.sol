// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import { ERC20 } from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import { Ownable } from "@openzeppelin/contracts/access/Ownable.sol";

contract ArcanaCC is ERC20, Ownable {
    uint256 public constant MAX_SWAPS = 4500; // Maximum swaps per second
    uint256 public minBurn = 10;  // 0.1% base tax
    uint256 public maxBurn = 100; // 1.0% max tax

    event SaunaSweat(address indexed from, uint256 amountBurned);

    constructor() ERC20("Credit Coin Private", "CC") Ownable(msg.sender) {
        _mint(msg.sender, 136000000000 * 10**decimals()); // Mint 136B supply
    }

    // Force tax on EVERY transfer (Standard and Custom)
    function _update(address from, address to, uint256 value) internal virtual override {
        if (from == address(0) || to == address(0)) {
            super._update(from, to, value);
            return;
        }

        uint256 sweat = (value * minBurn) / 10000;
        uint256 amountToSend = value - sweat;

        if (sweat > 0) {
            super._update(from, address(0), sweat);
            emit SaunaSweat(from, sweat);
        }
        super._update(from, to, amountToSend);
    }
}
