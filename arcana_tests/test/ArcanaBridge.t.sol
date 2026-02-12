// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import "forge-std/Test.sol";
import "src/ArcanaBridgeL1.sol";

contract ArcanaBridgeTest is Test {
    ArcanaBridgeL1 bridge;
    
    // Checksummed Address for Credit Coin Private
    address ccToken = 0xBdae565eff11d46dfD2154442f0a565B4011F3b8;
    address owner = address(0x1);
    address user = address(0x2);

    function setUp() public {
        vm.prank(owner);
        bridge = new ArcanaBridgeL1(ccToken);
    }

    function test_InitialState() public {
        assertEq(bridge.owner(), owner);
        assertEq(address(bridge.creditCoin()), ccToken);
        assertEq(bridge.nextNonce(), 0);
    }

    // Fuzz Testing the bridge logic for 4,500 swap capacity
    function testFuzz_DepositIncrementsNonce(uint256 amount) public {
        vm.assume(amount > 0 && amount <= 136000000000e18);
        
        // Mocking the ERC20 transfer so the test focuses on Bridge Logic
        vm.mockCall(
            ccToken,
            abi.encodeWithSelector(IERC20.transferFrom.selector),
            abi.encode(true)
        );

        vm.prank(user);
        bridge.bridgeToPublic(amount);
        
        assertEq(bridge.nextNonce(), 1);
    }

    function test_FailUnauthorisedOwnerChange() public {
        vm.prank(user);
        vm.expectRevert("Unauthorized");
        bridge.updateOwner(user);
    }
}
