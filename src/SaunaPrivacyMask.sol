// SPDX-License-Identifier: MIT
pragma solidity ^0.8.33;

import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {SafeERC20} from "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

contract SaunaPrivacyMask {
    using SafeERC20 for IERC20;

    IERC20 public immutable CREDIT_COIN;

    event MaskedDeposit(address indexed user, uint256 amount);

    constructor(address _creditCoin) {
        require(_creditCoin != address(0), "Invalid CC Address");
        CREDIT_COIN = IERC20(_creditCoin);
    }

    function depositToMask(uint256 amount) external {
        CREDIT_COIN.safeTransferFrom(msg.sender, address(this), amount);
        emit MaskedDeposit(msg.sender, amount);
    }
}
