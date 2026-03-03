// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IERC20 {
    function transferFrom(address src, address dst, uint wad) external returns (bool);
    function transfer(address dst, uint wad) external returns (bool);
}

contract PSM {
    address public admin;
    IERC20 public ccp;
    IERC20 public sausd;

    constructor(address _ccp, address _sausd) {
        admin = msg.sender;
        ccp = IERC20(_ccp);
        sausd = IERC20(_sausd);
    }

    function swapCCtoSA(uint256 amount) external {
        require(ccp.transferFrom(msg.sender, address(this), amount), "CC-P Transfer Failed");
        require(sausd.transfer(msg.sender, amount), "saUSD Transfer Failed");
    }
}
