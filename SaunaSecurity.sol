// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SaunaSecurity {
    bool private _locked;
    address public sovereign;
    uint256 public maxSwapLimit = 1000000000 * 10**18;

    constructor() {
        sovereign = msg.sender;
    }

    modifier saunaGuard() {
        require(!_locked, "SaunaProtocol: Reentrancy detected");
        _locked = true;
        _;
        _locked = false;
    }

    function checkProtocol() public view returns (string memory) {
        return "Sauna Security Active";
    }
}
