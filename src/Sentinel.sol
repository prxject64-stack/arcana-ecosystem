// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/access/AccessControl.sol";

interface IVault {
    function totalAssets() external view returns (uint256);
    function pause() external;
    function hasRole(bytes32 role, address account) external view returns (bool);
}

contract Sentinel is AccessControl {
    bytes32 public constant SENTINEL_ROLE = keccak256("SENTINEL_ROLE");
    IVault public immutable vault;
    uint256 public lastTotalAssets;
    uint256 public constant DRAIN_THRESHOLD_PERCENT = 10;

    event LiquidityDrainDetected(uint256 amountDrained, uint256 percentOfSupply);
    event VaultPaused(address indexed trigger);

    constructor(address _vault) {
        vault = IVault(_vault);
        lastTotalAssets = vault.totalAssets();
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
    }

    function monitorReserves() external onlyRole(SENTINEL_ROLE) {
        uint256 currentAssets = vault.totalAssets();
        uint256 threshold = (lastTotalAssets * DRAIN_THRESHOLD_PERCENT) / 100;

        if (lastTotalAssets > currentAssets && (lastTotalAssets - currentAssets) >= threshold) {
            emit LiquidityDrainDetected(lastTotalAssets - currentAssets, DRAIN_THRESHOLD_PERCENT);
            vault.pause();
            emit VaultPaused(msg.sender);
        }
        
        lastTotalAssets = currentAssets;
    }

    function updateBaseline() external onlyRole(SENTINEL_ROLE) {
        lastTotalAssets = vault.totalAssets();
    }
}
