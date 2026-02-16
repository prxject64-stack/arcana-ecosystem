 // SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract CreditCoinPrivate is ERC20 {
    constructor() ERC20("Credit Coin Private", "CC") {
        _mint(0x4f9595e22a0881b1a13f9ac039b45a3eb56d6497, 136000000000 * 10**decimals());
    }
}
