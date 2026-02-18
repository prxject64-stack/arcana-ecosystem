async function main() {
  const CC_ADDR = '0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512';
  const TR = '0x322813fd9a05da47206818293028c39ed8b00000';
  const ghost1 = '0x322813Fd9A801c5507c9de605d63CEA4f2CE6c44';
  const ghost2 = '0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0';

  const cc = await ethers.getContractAt('contracts/IERC20.sol:IERC20', CC_ADDR);

  for (const ghost of [ghost1, ghost2]) {
    console.log(`Attempting Impersonation of ${ghost}...`);
    await network.provider.request({
      method: "hardhat_impersonateAccount",
      params: [ghost],
    });

    const ghostSigner = await ethers.getSigner(ghost);
    
    // We need ETH in the ghost wallet to pay for the transfer gas
    const [admin] = await ethers.getSigners();
    await admin.sendTransaction({ to: ghost, value: ethers.parseEther("1.0") });

    const bal = await cc.balanceOf(ghost);
    if (bal > 0n) {
      await cc.connect(ghostSigner).transfer(TR, bal);
      console.log(`RECOVERED ${ethers.formatUnits(bal, 18)} CC from ${ghost}`);
    }

    await network.provider.request({
      method: "hardhat_stopImpersonatingAccount",
      params: [ghost],
    });
  }
}
main().catch(console.error);
