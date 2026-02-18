// SPDX-License-Identifier: MIT
pragma solidity ^0.8.33;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SovereignUSD is ERC20, Ownable {
    mapping(address => bool) public minters;

    event SyntheticIssuance(address indexed to, uint256 amount, string reason);

    constructor() ERC20("Sovereign USD", "sUSD") Ownable(msg.sender) {}

    modifier onlyMinter() {
        require(minters[msg.sender] || owner() == msg.sender, "sUSD: Not authorized");
        _;
    }

    function addMinter(address _minter) external onlyOwner {
        minters[_minter] = true;
    }

    function syntheticMint(address to, uint256 amount, string memory reason) external onlyMinter {
        _mint(to, amount);
        emit SyntheticIssuance(to, amount, reason);
    }

    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
