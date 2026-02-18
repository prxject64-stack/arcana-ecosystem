async function main() {
  const CC_ADDR = '0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512';
  const TR = '0x322813fd9a05da47206818293028c39ed8b00000';
  const ghost1 = '0x322813Fd9A801c5507c9de605d63CEA4f2CE6c44';
  const ghost2 = '0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0';
  
  const signers = await ethers.getSigners();
  const cc = await ethers.getContractAt('contracts/IERC20.sol:IERC20', CC_ADDR);

  for (const ghost of [ghost1, ghost2]) {
    const bal = await cc.balanceOf(ghost);
    console.log(`Checking Ghost ${ghost}: ${ethers.formatUnits(bal, 18)} CC`);
    
    const owner = signers.find(s => s.address.toLowerCase() === ghost.toLowerCase());
    if (owner) {
      console.log(`SUCCESS: You own this ghost! Transferring to Treasury...`);
      const tx = await cc.connect(owner).transfer(TR, bal);
      await tx.wait();
    } else {
      console.log(`CRITICAL: You do NOT own ${ghost} in this session.`);
    }
  }
}
main().catch(console.error);
