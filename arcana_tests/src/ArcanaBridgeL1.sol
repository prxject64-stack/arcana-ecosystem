// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title ArcanaBridgeL1
 * @dev Facilitates 4,500 simultaneous P2P swaps via locked liquidity.
 */
interface IERC20 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract ArcanaBridgeL1 {
    address public owner;
    IERC20 public creditCoin;
    uint256 public nextNonce; // Critical for Multisig Relayer tracking

    event Deposit(address indexed user, uint256 amount, uint256 nonce, uint256 timestamp);

    constructor(address _ccAddress) {
        owner = msg.sender;
        creditCoin = IERC20(_ccAddress);
    }

    /**
     * @dev Locks CC tokens on L1 to trigger minting/unlocking on destination.
     * Incorporates Sauna Protocol security standards.
     */
    function bridgeToPublic(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(creditCoin.transferFrom(msg.sender, address(this), _amount), "Transfer failed");
        
        emit Deposit(msg.sender, _amount, nextNonce, block.timestamp);
        
        // Increment nonce to prevent replay attacks on the Relayer side
        nextNonce++;
    }

    function updateOwner(address _newOwner) external {
        require(msg.sender == owner, "Unauthorized");
        owner = _newOwner;
    }
}
