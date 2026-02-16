// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract SaunaPrivacyMask {
    IERC20 public immutable creditCoin;

    constructor(address _creditCoin) {
        creditCoin = IERC20(_creditCoin);
    }

    function deposit(uint256 amount) external {
        creditCoin.transferFrom(msg.sender, address(this), amount);
    }
}
