// SPDX-License-Identifier: MIT
pragma solidity 0.8.33;

import {ERC20} from "lib/openzeppelin-contracts/contracts/token/ERC20/ERC20.sol";
import {Ownable} from "lib/openzeppelin-contracts/contracts/access/Ownable.sol";

contract ArcanaSovereign is ERC20, Ownable {
    constructor() ERC20("Arcana Sovereign", "ARC") Ownable(msg.sender) {
        // Minting 1B ARC to the deployer for initial ecosystem liquidity
        _mint(msg.sender, 1_000_000_000 * 10**decimals());
    }

    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
}
