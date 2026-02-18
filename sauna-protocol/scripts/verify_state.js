const hre = require('hardhat');
async function main() {
  const sUSDAddress = '0x57ab1ec28d129707052df4df418d58a2d46d5f51';
  const whaleAddress = '0x8ad525046270b200b6526131b7f03673c68383e9';
  const sUSD = await hre.ethers.getContractAt('IERC20', sUSDAddress);
  const balance = await sUSD.balanceOf(whaleAddress);
  console.log('--- POST-SWAP VERIFICATION ---');
  console.log('Whale sUSD Remaining: ' + hre.ethers.formatUnits(balance, 18));
}
main().catch(console.error);
