// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract ArcanaIdentity {
    address public admin;
    mapping(address => bool) public isVerified;

    event IdentityVerified(address indexed user);
    event IdentityRevoked(address indexed user);

    constructor() {
        admin = msg.sender;
    }

    modifier onlyAdmin() {
        require(msg.sender == admin, "Sauna: Unauthorized");
        _;
    }

    function verifyUser(address _user) external onlyAdmin {
        isVerified[_user] = true;
        emit IdentityVerified(_user);
    }

    function revokeUser(address _user) external onlyAdmin {
        isVerified[_user] = false;
        emit IdentityRevoked(_user);
    }
}
