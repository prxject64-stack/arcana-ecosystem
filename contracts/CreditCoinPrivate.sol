// SPDX-License-Identifier: MIT
pragma solidity ^0.8.33;

import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CreditCoinPrivate (CC)
 * @notice Initial Supply: 136,000,000,000 CC
 */
contract CreditCoinPrivate is ERC20, Ownable {
    
    // Checksummed Sovereign Vault Address
    address public constant SOVEREIGN_VAULT = 0x4F9595e22A0881B1a13F9AC039B45a3Eb56D6497;

    constructor() ERC20("Credit Coin Private", "CC") Ownable(msg.sender) {
        // Minting the full 136B CC to the vault
        _mint(SOVEREIGN_VAULT, 136_000_000_000 * 10**decimals());
    }

    /**
     * @dev Protocol-level minting for labor rewards
     */
    function mintSovereignReward(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }
}
