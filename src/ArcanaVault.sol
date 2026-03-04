// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/utils/Pausable.sol";

contract ArcanaVault is AccessControl, Pausable {
    bytes32 public constant PAUSER_ROLE = keccak256("PAUSER_ROLE");
    IERC20 public arcS;
    IERC20 public saUSD;
    mapping(address => uint256) public collateral;

    constructor(address _arcS, address _saUSD) {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        arcS = IERC20(_arcS);
        saUSD = IERC20(_saUSD);
    }

    function pause() external onlyRole(PAUSER_ROLE) { _pause(); }
    function unpause() external onlyRole(DEFAULT_ADMIN_ROLE) { _unpause(); }

    function depositCollateral(uint256 _amount) external whenNotPaused {
        arcS.transferFrom(msg.sender, address(this), _amount);
        collateral[msg.sender] += _amount;
    }

    function mintStable(uint256 _amount) external whenNotPaused {
        uint256 value = collateral[msg.sender];
        require(value >= _amount * 2, "Under-collateralized");
        saUSD.transfer(msg.sender, _amount);
    }
}