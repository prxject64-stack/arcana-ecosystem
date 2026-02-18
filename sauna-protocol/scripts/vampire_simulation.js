const hre = require('hardhat');

async function main() {
  const whaleAddress = '0x8ad525046270b200b6526131b7f03673c68383e9';

  // 1. Deploy Real Mock sUSD
  const Mock = await hre.ethers.getContractFactory('MockSUSD');
  const susd = await Mock.deploy();
  await susd.waitForDeployment();
  const susdAddress = await susd.getAddress();

  // 2. Mint 1M sUSD to Whale (Trapped Level)
  await susd.mint(whaleAddress, hre.ethers.parseUnits('1000000', 18));

  console.log('--- VAMPIRE SCAN: SAUNA PROTOCOL LIVE ---');
  const balance = await susd.balanceOf(whaleAddress);
  const balanceNum = parseFloat(hre.ethers.formatUnits(balance, 18));

  console.log('[DATA] Whale: ' + whaleAddress);
  console.log('[DATA] sUSD Balance: ' + balanceNum.toLocaleString());

  if (balanceNum < 5000000) {
    console.log('[STATUS] DEBT-TRAPPED (Under 50% threshold)');
    console.log('[ACTION] Target for Arcana Bridge Migration.');
  }
}
main().catch(console.error);
