// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

contract ArcanaAMM is AccessControl, ReentrancyGuard {
    bytes32 public constant GOVERNOR_ROLE = keccak256("GOVERNOR_ROLE");
    IERC20 public saUSD;
    IERC20 public ccP;
    IERC20 public arcS;
    uint256 public reserveSaUSD;
    uint256 public reserveCCP;

    constructor(address _saUSD, address _ccP, address _arcS) {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        saUSD = IERC20(_saUSD);
        ccP = IERC20(_ccP);
        arcS = IERC20(_arcS);
    }

    function addLiquidity(uint256 _amountSaUSD, uint256 _amountCCP) external onlyRole(DEFAULT_ADMIN_ROLE) {
        saUSD.transferFrom(msg.sender, address(this), _amountSaUSD);
        ccP.transferFrom(msg.sender, address(this), _amountCCP);
        reserveSaUSD += _amountSaUSD;
        reserveCCP += _amountCCP;
    }

    function swap(uint256 _amountIn) external nonReentrant returns (uint256 amountOut) {
        require(reserveCCP > 0 && reserveSaUSD > 0, "No Liquidity");
        amountOut = (reserveSaUSD * _amountIn) / (reserveCCP + _amountIn);
        ccP.transferFrom(msg.sender, address(this), _amountIn);
        saUSD.transfer(msg.sender, amountOut);
        reserveCCP += _amountIn;
        reserveSaUSD -= amountOut;
    }
}