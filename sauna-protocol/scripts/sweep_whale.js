async function main() {
  const CC_ADDR = '0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512';
  const TR = '0x322813fd9a05da47206818293028c39ed8b00000';
  const signers = await ethers.getSigners();
  const whale = signers[1]; // Account #1
  const cc = await ethers.getContractAt('contracts/IERC20.sol:IERC20', CC_ADDR, whale);
  
  const bal = await cc.balanceOf(whale.address);
  console.log('Sweeping', ethers.formatUnits(bal, 18), 'CC from Account #1...');
  const tx = await cc.transfer(TR, bal);
  await tx.wait();
  console.log('Treasury funded.');
}
main().catch(console.error);
