// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract ArcanaVault {
    IERC20 public arcS;
    IERC20 public saUSD;
    mapping(address => uint256) public collateral;

    constructor(address _arcS, address _saUSD) {
        arcS = IERC20(_arcS);
        saUSD = IERC20(_saUSD);
    }

    function depositCollateral(uint256 _amount) external {
        arcS.transferFrom(msg.sender, address(this), _amount);
        collateral[msg.sender] += _amount;
    }

    function mintStable(uint256 _amount) external {
        uint256 value = collateral[msg.sender];
        require(value >= _amount * 2, "Under-collateralized");
        saUSD.transfer(msg.sender, _amount);
    }
}