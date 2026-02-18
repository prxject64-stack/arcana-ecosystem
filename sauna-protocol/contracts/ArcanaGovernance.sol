// SPDX-License-Identifier: MIT
pragma solidity ^0.8.33;

import "@openzeppelin/contracts/access/Ownable.sol";

contract ArcanaGovernance is Ownable {
    uint256 public constant PROPOSAL_THRESHOLD = 1000000 * 10**18; // 1M CC to propose
    uint256 public totalProposals;

    struct Proposal {
        address target;
        uint256 value;
        string description;
        bool executed;
    }

    mapping(uint256 => Proposal) public proposals;

    constructor() Ownable(msg.sender) {}

    function createProposal(address _target, uint256 _value, string memory _description) external onlyOwner {
        proposals[totalProposals] = Proposal(_target, _value, _description, false);
        totalProposals++;
    }

    function executeProposal(uint256 _id) external onlyOwner {
        Proposal storage p = proposals[_id];
        require(!p.executed, "GOV: Already executed");
        p.executed = true;
        (bool success, ) = p.target.call{value: 0}(abi.encodeWithSignature("transfer(address,uint256)", owner(), p.value));
        require(success, "GOV: Execution failed");
    }
}
