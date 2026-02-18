const hre = require('hardhat');

async function main() {
  const sUSDAddress = '0x57ab1ec28d129707052df4df418d58a2d46d5f51';
  const targetWhales = [
    '0x8ad525046270b200b6526131b7f03673c68383e9',
    '0x4A92d04a609600e1E5E5830d9E7D88b637508092'
  ];

  // Verify contract bytecode exists at address
  const code = await hre.ethers.provider.getCode(sUSDAddress);
  if (code === '0x') {
    console.log('[CRITICAL] sUSD contract not found at address on this network.');
    process.exit(1);
  }

  const abi = ['function balanceOf(address account) view returns (uint256)'];
  const sUSD = await hre.ethers.getContractAt(abi, sUSDAddress);

  console.log('--- SCANNING FOR DEBT-TRAPPED WHALES (50% THRESHOLD) ---');

  for (const whale of targetWhales) {
    try {
      const balance = await sUSD.balanceOf(whale);
      const balanceNum = parseFloat(hre.ethers.formatUnits(balance, 18));

      // SIP-420 Rule: 50% threshold for Jubilee
      if (balanceNum < 5000000) {
        console.log('[TARGET] Whale ' + whale + ': ' + balanceNum.toLocaleString() + ' sUSD (FROZEN)');
      } else {
        console.log('[SAFE] Whale ' + whale + ': ' + balanceNum.toLocaleString() + ' sUSD');
      }
    } catch (e) {
      console.log('[ERROR] Interaction failed for ' + whale + '. Check provider connection.');
    }
  }
}
main().catch(console.error);
