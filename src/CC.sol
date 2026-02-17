// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract CC is ERC20 {
    constructor() ERC20("Credit Coin Private", "CC") {
        // Minting your 136 Billion CC
        _mint(msg.sender, 136000000000 * 10**decimals());
    }
}
