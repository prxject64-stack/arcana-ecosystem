// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SaunaVault is Ownable {
    IERC20 public saUSD;
    mapping(address => uint256) public deposits;

    event Deposited(address indexed user, uint256 amount);

    constructor(address _saUSD) Ownable(msg.sender) {
        saUSD = IERC20(_saUSD);
    }

    function deposit(uint256 amount) external {
        require(saUSD.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        deposits[msg.sender] += amount;
        emit Deposited(msg.sender, amount);
    }
}
