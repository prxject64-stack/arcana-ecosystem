// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IERC20 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
}

contract ArcanaBridgeL1 {
    address public owner;
    IERC20 public creditCoin;

    event Deposit(address indexed user, uint256 amount, uint256 timestamp);

    constructor(address _ccAddress) {
        owner = msg.sender;
        creditCoin = IERC20(_ccAddress);
    }

    function bridgeToPublic(uint256 _amount) external {
        require(creditCoin.transferFrom(msg.sender, address(this), _amount), "Transfer failed");
        emit Deposit(msg.sender, _amount, block.timestamp);
    }
}
