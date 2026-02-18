// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract SovereignDollar is ERC20 {
    address public vault;
    constructor() ERC20("Sovereign Dollar", "sUSD") { vault = msg.sender; }
    function mint(address to, uint256 amount) external {
        require(msg.sender == vault, "Only Vault");
        _mint(to, amount);
    }
    function burn(address from, uint256 amount) external {
        require(msg.sender == vault, "Only Vault");
        _burn(from, amount);
    }
}

contract SaunaVault {
    SovereignDollar public sUSD;
    IERC20 public arcToken; // Your ARC coin
    
    struct Position { uint256 collateral; uint256 debt; uint256 timestamp; }
    mapping(address => Position) public positions;
    
    uint256 public constant RATIO = 150; 
    uint256 public constant STABILITY_FEE = 5; // 5% Annual Interest

    constructor(address _sUSD, address _arc) {
        sUSD = SovereignDollar(_sUSD);
        arcToken = IERC20(_arc);
    }

    function depositAndMint(uint256 mintAmount) external payable {
        uint256 req = (mintAmount * RATIO) / 100;
        require(msg.value >= req, "Insufficient CC");
        positions[msg.sender].collateral += msg.value;
        positions[msg.sender].debt += mintAmount;
        positions[msg.sender].timestamp = block.timestamp;
        sUSD.mint(msg.sender, mintAmount);
    }

    // To unlock CC, they pay sUSD + ARC fee
    function repayAndWithdraw(uint256 repayAmount, uint256 arcFee) external {
        require(positions[msg.sender].debt >= repayAmount, "Over-repaying");
        // Logic: arcFee would be calculated based on (block.timestamp - positions.timestamp)
        arcToken.transferFrom(msg.sender, address(this), arcFee); 
        sUSD.burn(msg.sender, repayAmount);
        positions[msg.sender].debt -= repayAmount;
        payable(msg.sender).transfer(positions[msg.sender].collateral);
    }
}
