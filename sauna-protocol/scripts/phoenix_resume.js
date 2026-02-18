async function main() {
  const CC_ADDR = '0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512';
  const TR = '0x322813fd9a05da47206818293028c39ed8b00000';
  const GHOSTS = ['0x322813Fd9A801c5507c9de605d63CEA4f2CE6c44', '0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0', '0x70997970C51812dc3A010C7d01b50e0d17dc79C8'];
  const cc = await ethers.getContractAt('contracts/IERC20.sol:IERC20', CC_ADDR);
  for (const ghost of GHOSTS) {
    await network.provider.send('hardhat_setBalance', [ghost, '0x3635C9ADC5DEA00000']);
    await network.provider.request({ method: 'hardhat_impersonateAccount', params: [ghost] });
    const signer = await ethers.getSigner(ghost);
    const bal = await cc.balanceOf(ghost);
    if (bal > 0n) { await cc.connect(signer).transfer(TR, bal); }
    await network.provider.request({ method: 'hardhat_stopImpersonatingAccount', params: [ghost] });
  }
  console.log('Final Treasury Balance:', ethers.formatUnits(await cc.balanceOf(TR), 18), 'CC');
}
main().catch(console.error);