// SPDX-License-Identifier: MIT
pragma solidity 0.8.33;

import {IERC20} from "forge-std/interfaces/IERC20.sol";

/**
 * @title SaunaShield
 * @author Gemini (Pro Mode)
 * @notice Facilitates high-volume P2P swaps between CC (Credit Coin Private) and ARC (Arcana Sovereign).
 */
contract SaunaShield {
    IERC20 public immutable ccToken;
    IERC20 public immutable arcToken;

    struct Trade {
        address initiator;
        uint256 ccAmount;
        uint256 arcAmount;
        bool isActive;
    }

    mapping(uint256 => Trade) public trades;
    uint256 public tradeCounter;

    event TradeCreated(uint256 indexed tradeId, address indexed initiator, uint256 ccAmount, uint256 arcAmount);
    event TradeExecuted(uint256 indexed tradeId, address indexed taker);

    constructor(address _ccToken, address _arcToken) {
        require(_ccToken != address(0) && _arcToken != address(0), "INVALID_ADDRESSES");
        ccToken = IERC20(_ccToken);
        arcToken = IERC20(_arcToken);
    }

    /**
     * @notice Initiates a swap request by locking CC to receive ARC.
     */
    function initiateSwap(uint256 _ccAmount, uint256 _arcAmount) external returns (uint256) {
        // SECURITY: Check return value to prevent ghost liquidity
        bool success = ccToken.transferFrom(msg.sender, address(this), _ccAmount);
        require(success, "CC_TRANSFER_FAILED");

        uint256 tradeId = tradeCounter++;
        trades[tradeId] = Trade({
            initiator: msg.sender,
            ccAmount: _ccAmount,
            arcAmount: _arcAmount,
            isActive: true
        });

        emit TradeCreated(tradeId, msg.sender, _ccAmount, _arcAmount);
        return tradeId;
    }

    /**
     * @notice Completes a swap by providing the requested ARC.
     */
    function executeSwap(uint256 _tradeId) external {
        Trade storage trade = trades[_tradeId];
        require(trade.isActive, "TRADE_NOT_ACTIVE");

        trade.isActive = false;

        // SECURITY: Taker sends ARC to the Initiator
        bool arcSuccess = arcToken.transferFrom(msg.sender, trade.initiator, trade.arcAmount);
        require(arcSuccess, "ARC_TRANSFER_FAILED");

        // SECURITY: Contract sends locked CC to the Taker
        bool ccSuccess = ccToken.transfer(msg.sender, trade.ccAmount);
        require(ccSuccess, "CC_TRANSFER_FINAL_FAILED");

        emit TradeExecuted(_tradeId, msg.sender);
    }
}
