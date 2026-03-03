// SPDX-License-Identifier: MIT
pragma solidity 0.8.28;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SaunaVault is Ownable {
    IERC20 public saUSD;

    constructor(address _saUSD, address _initialOwner) Ownable(_initialOwner) {
        saUSD = IERC20(_saUSD);
    }

    function deposit(uint256 amount) external {
        require(saUSD.transferFrom(msg.sender, address(this), amount), "Transfer failed");
    }
}
