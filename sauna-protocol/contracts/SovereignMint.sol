// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract SovereignDollar is ERC20 {
    constructor() ERC20("Sovereign Dollar", "sUSD") {}

    function mint(address to, uint256 amount) external {
        // Only the Sauna Vault can call this
        _mint(to, amount);
    }
}

contract SaunaVault {
    SovereignDollar public sUSD;
    mapping(address => uint256) public collateral;
    uint256 public constant RATIO = 150; // 150% requirement

    constructor(address _sUSD) {
        sUSD = SovereignDollar(_sUSD);
    }

    function depositAndMint(uint256 mintAmount) external payable {
        // Raw Data: We assume 1 CC = 1 USD for the boot phase
        uint256 requiredCollateral = (mintAmount * RATIO) / 100;
        require(msg.value >= requiredCollateral, "Insufficient CC Collateral");
        
        collateral[msg.sender] += msg.value;
        sUSD.mint(msg.sender, mintAmount);
    }
}
