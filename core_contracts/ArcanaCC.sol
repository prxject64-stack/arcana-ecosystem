// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import { ERC20 } from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
contract ArcanaCC is ERC20 {
    constructor() ERC20("Credit Coin Private", "CC") {
        _mint(msg.sender, 136000000000 * 10**18);
    }
}
