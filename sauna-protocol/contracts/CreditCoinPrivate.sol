// SPDX-License-Identifier: MIT
pragma solidity ^0.8.33;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CreditCoinPrivate is ERC20, Ownable {
    constructor() ERC20("Credit Coin Private", "CC") Ownable(msg.sender) {
        // Mint 136 Billion with 18 decimals
        _mint(msg.sender, 136000000000 * 10**decimals());
    }
}
