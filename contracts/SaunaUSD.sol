// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SaunaUSD is ERC20, Ownable {
    constructor() ERC20("Sauna USD", "saUSD") Ownable(msg.sender) {
        // Mint initial supply to the Sovereign Master
        _mint(msg.sender, 1000000000 * 10**decimals()); // 1B saUSD
    }

    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
}
