const hre = require('hardhat');

async function main() {
  const bridgeAddress = '0x5FbDB2315678afecb367f032d93F642f64180aa3';
  const sUSDAddress = '0x57ab1ec28d129707052df4df418d58a2d46d5f51';
  const whaleAddress = '0x8ad525046270b200b6526131b7f03673c68383e9';

  // 1. Impersonate and Fund the Whale with GAS (ETH)
  await hre.network.provider.request({ method: 'hardhat_impersonateAccount', params: [whaleAddress] });
  await hre.network.provider.send('hardhat_setBalance', [
    whaleAddress,
    '0x3635C9ADC5DEA00000', // 1,000 ETH in Hex
  ]);
  
  const whale = await hre.ethers.getSigner(whaleAddress);
  const amount = hre.ethers.parseUnits('10000000', 18);

  // 2. Mock 10M sUSD Balance
  await hre.network.provider.send('hardhat_setStorageAt', [sUSDAddress, '0x3', hre.ethers.zeroPadValue(hre.ethers.toBeHex(amount), 32)]);

  const bridge = await hre.ethers.getContractAt('SovereignBridge', bridgeAddress, whale);

  console.log('[INFO] Whale Funded with 1,000 ETH. Executing 10M sUSD Swap...');
  
  const tx = await bridge.swap(amount);
  await tx.wait();

  console.log('[SUCCESS] 10,000,000 sUSD Stress Test Passed. Hash: ' + tx.hash);
}

main().catch((error) => { console.error(error); });
