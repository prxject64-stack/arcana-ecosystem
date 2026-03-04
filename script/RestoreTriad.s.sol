import "forge-std/Script.sol";
import "../src/ArcanaAMM.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract RestoreTriad is Script {
    function run() external {
        address token = 0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512;
        uint256 amount = 40000000000000000000000000000;
        vm.startBroadcast();
        ArcanaAMM amm = new ArcanaAMM(token, token, 0x5FbDB2315678afecb367f032d93F642f64180aa3);
        IERC20(token).approve(address(amm), amount * 2);
        amm.addLiquidity(amount, amount);
        vm.stopBroadcast();
        console.log("NEW_AMM_ADDRESS:", address(amm));
    }
}