// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface ICCPrivate {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract ArcanaPassport {
    ICCPrivate public ccToken;
    address public constant BURN_ADDRESS = 0x0000000000000000000000000000000000000000;
    uint256 public constant SACRIFICE_AMOUNT = 100 * 10**18;

    mapping(address => bool) public isCitizen;
    uint256 public totalCitizens;

    event Naturalized(address indexed citizen, uint256 timestamp);

    constructor(address _ccTokenAddress) {
        ccToken = ICCPrivate(_ccTokenAddress);
    }

    function performSacrifice() external {
        require(!isCitizen[msg.sender], "Already a Citizen of Arcana");
        require(ccToken.balanceOf(msg.sender) >= SACRIFICE_AMOUNT, "Insufficient CC");
        require(ccToken.transferFrom(msg.sender, BURN_ADDRESS, SACRIFICE_AMOUNT), "Burn Failed");

        isCitizen[msg.sender] = true;
        totalCitizens++;
        emit Naturalized(msg.sender, block.timestamp);
    }
}
