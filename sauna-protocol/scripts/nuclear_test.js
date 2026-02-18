const hre = require('hardhat');

async function main() {
  const sUSDAddress = '0x57ab1ec28d129707052df4df418d58a2d46d5f51';
  const whaleAddress = '0x8ad525046270b200b6526131b7f03673c68383e9';

  // 1. Deploy Fresh Bridge
  const Bridge = await hre.ethers.getContractFactory('SovereignBridge');
  const bridge = await Bridge.deploy('0x5FbDB2315678afecb367f032d93F642f64180aa3');
  await bridge.waitForDeployment();
  const bridgeAddress = await bridge.getAddress();
  console.log('[DEPLOYED] Bridge at: ' + bridgeAddress);

  // 2. Impersonate and Fund Whale
  await hre.network.provider.request({ method: 'hardhat_impersonateAccount', params: [whaleAddress] });
  await hre.network.provider.send('hardhat_setBalance', [whaleAddress, '0x3635C9ADC5DEA00000']);
  const whale = await hre.ethers.getSigner(whaleAddress);

  // 3. Mock 10M sUSD Balance
  const amount = hre.ethers.parseUnits('10000000', 18);
  await hre.network.provider.send('hardhat_setStorageAt', [sUSDAddress, '0x3', hre.ethers.zeroPadValue(hre.ethers.toBeHex(amount), 32)]);

  // 4. Execute Swap
  console.log('[ACTION] Whale executing 10M sUSD swap...');
  const tx = await bridge.connect(whale).swap(amount);
  await tx.wait();

  console.log('[SUCCESS] 10,000,000 sUSD Stress Test Passed. Hash: ' + tx.hash);
}
main().catch((error) => { console.error(error); });
