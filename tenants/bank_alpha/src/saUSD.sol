// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract SaunaUSD is ERC20 {
    constructor(uint256 initialSupply) ERC20("Sauna USD", "saUSD") {
        _mint(msg.sender, initialSupply * 10**decimals());
    }
}
