// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/metatx/ERC2771Context.sol";
import "@aave/core-v3/contracts/flashloan/base/FlashLoanSimpleReceiverBase.sol";

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract GaslessArb is ERC2771Context, FlashLoanSimpleReceiverBase {
    constructor(address _addressProvider, address _forwarder) 
        ERC2771Context(_forwarder)
        FlashLoanSimpleReceiverBase(IPoolAddressesProvider(_addressProvider)) 
    {}

    function executeOperation(
        address asset,
        uint256 amount,
        uint256 premium,
        address initiator,
        bytes calldata params
    ) external override returns (bool) {
        uint256 amountToRepay = amount + premium;
        IERC20(asset).approve(address(POOL), amountToRepay);
        
        uint256 totalBalance = IERC20(asset).balanceOf(address(this));
        if (totalBalance > amountToRepay) {
            uint256 profit = totalBalance - amountToRepay;
            IERC20(asset).transfer(_msgSender(), profit);
        }
        return true;
    }

    function _msgSender() internal view override(Context, ERC2771Context) returns (address) {
        return ERC2771Context._msgSender();
    }

    function _msgData() internal view override(Context, ERC2771Context) returns (bytes calldata) {
        return ERC2771Context._msgData();
    }
}
