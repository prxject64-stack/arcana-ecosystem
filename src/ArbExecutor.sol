// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract ArbExecutor is Ownable {
    address public principal;
    mapping(address => bool) public isAuth;

    event PrincipalSet(address indexed newPrincipal);

    constructor() Ownable(msg.sender) {}

    function setPrincipal(address _principal) external onlyOwner {
        principal = _principal;
        isAuth[_principal] = true;
        emit PrincipalSet(_principal);
    }

    function executeSwap(address token, address to, uint256 amount) external {
        require(msg.sender == owner() || msg.sender == principal, "Not authorized");
        IERC20(token).transfer(to, amount);
    }
    
    // Logic for 4,500 simultaneous swaps would go here
}
