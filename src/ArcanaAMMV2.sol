// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/utils/Pausable.sol";

contract ArcanaAMMV2 is AccessControl, Pausable {
    bytes32 public constant PAUSER_ROLE = keccak256("PAUSER_ROLE");
    IERC20 public ccP;
    IERC20 public saUSD;

    constructor(address _ccP, address _saUSD) {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        ccP = IERC20(_ccP);
        saUSD = IERC20(_saUSD);
    }

    function pause() external onlyRole(PAUSER_ROLE) { _pause(); }
    function unpause() external onlyRole(DEFAULT_ADMIN_ROLE) { _unpause(); }

    function swapCCForUSD(uint256 _amount) external whenNotPaused {
        ccP.transferFrom(msg.sender, address(this), _amount);
        uint256 out = _amount * 2; // Fixed Stress Test Ratio
        saUSD.transfer(msg.sender, out);
    }
    function reserveCCP() public view returns (uint256) { return ccP.balanceOf(address(this)); }
    function reserveSAUSD() public view returns (uint256) { return saUSD.balanceOf(address(this)); }
}