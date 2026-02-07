// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CreditCoin is ERC20, Ownable {
    constructor() 
        ERC20("Credit Coin Private", "CC") 
        Ownable(msg.sender) 
    {
        // Minting 136 Billion CC to the deployer (Boss Key)
        _mint(msg.sender, 136000000000 * 10**decimals());
    }

    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
}
