// SPDX-License-Identifier: MIT
pragma solidity ^0.8.33;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract MerchantTerminal {
    address public sUSD;
    address public owner;

    event Purchase(address indexed buyer, string item, uint256 cost);

    constructor(address _sUSD) {
        sUSD = _sUSD;
        owner = msg.sender;
    }

    function buyItem(string memory itemName, uint256 cost) external {
        require(IERC20(sUSD).transferFrom(msg.sender, owner, cost), "Payment failed");
        emit Purchase(msg.sender, itemName, cost);
    }
}
