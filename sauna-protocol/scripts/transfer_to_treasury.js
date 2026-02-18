async function main() {
  const CC='0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512';
  const TR='0x322813fd9a05da47206818293028c39ed8b00000';
  const [signer] = await ethers.getSigners();
  const cc = await ethers.getContractAt('contracts/IERC20.sol:IERC20', CC);
  const bal = await cc.balanceOf(signer.address);
  console.log('Deployer has:', ethers.formatUnits(bal, 18));
  if(bal > 0n) {
    console.log('Transferring to Treasury...');
    const tx = await cc.transfer(TR, bal);
    await tx.wait();
    console.log('Transfer complete.');
  } else { console.log('Deployer is empty. No funds to transfer.'); }
}
main().catch((e) => { console.error(e); process.exit(1); });