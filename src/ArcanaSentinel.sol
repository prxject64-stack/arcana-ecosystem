// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/access/Ownable.sol";

interface ISaunaVault {
    function pause() external;
    function totalSupply() external view returns (uint256);
}

contract ArcanaSentinel is Ownable {
    ISaunaVault public immutable vault;
    uint256 public constant MAX_BLOCK_VOL_PCT = 10; // 10%

    event SecurityAlert(string reason, uint256 amount);

    constructor(address _vault) Ownable(msg.sender) {
        vault = ISaunaVault(_vault);
    }

    function validateVolume(uint256 _amount) external {
        uint256 supply = vault.totalSupply();
        if (supply > 0 && _amount > (supply * MAX_BLOCK_VOL_PCT) / 100) {
            vault.pause();
            emit SecurityAlert("Excessive Volume Detected", _amount);
        }
    }
}
