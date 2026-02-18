// SPDX-License-Identifier: MIT
pragma solidity ^0.8.33;
import "@openzeppelin/contracts/access/Ownable.sol";
contract ArcanaSentry is Ownable {
    address public saunaProtocol;
    uint256 public whaleThreshold;
    bool public monitoringActive;
    event WhaleAlert(address indexed offender, uint256 amount);
    constructor(address _sauna) Ownable(msg.sender) {
        saunaProtocol = _sauna;
        whaleThreshold = 100000000 * 10**18;
        monitoringActive = true;
    }
}
