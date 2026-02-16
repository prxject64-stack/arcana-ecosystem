// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CCPrivate is ERC20, Ownable {
    // 136 Billion CC with 18 decimals
    uint256 private constant INITIAL_SUPPLY = 136000000000 * 10**18;

    constructor() ERC20("Credit Coin Private", "CC") Ownable(msg.sender) {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // Pro Mode: Facilitate the 4,500 simultaneous swaps by allowing bulk approvals
    function bulkApprove(address spender, uint256 amount) external {
        _approve(msg.sender, spender, amount);
    }
}
