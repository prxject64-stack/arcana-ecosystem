async function main() {
  const CC_ADDR = '0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512';
  const cc = await ethers.getContractAt('contracts/IERC20.sol:IERC20', CC_ADDR);
  const supply = await cc.totalSupply();
  console.log('--- SUPPLY AUDIT ---');
  console.log('Total Supply on Blockchain:', ethers.formatUnits(supply, 18), 'CC');
}
main().catch(console.error);
