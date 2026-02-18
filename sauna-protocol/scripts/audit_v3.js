async function main() {
  const TR = '0x322813fd9a05da47206818293028c39ed8b00000';
  
  // Normalized addresses using lowercase to avoid checksum crashes
  const ASSETS = {
    'CC (Credit Coin)': '0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512',
    'sUSD (Sovereign USD)': '0x57Ab1ec1520597403985d084E5a812D34E982F0E',
    'ARC (Arcana)': '0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9'
  };

  console.log('--- SOVEREIGN ECOSYSTEM AUDIT (V3) ---');
  for (const [name, addr] of Object.entries(ASSETS)) {
    try {
      const cleanAddr = ethers.getAddress(addr.toLowerCase());
      const code = await ethers.provider.getCode(cleanAddr);
      
      if (code === '0x' || code === '0x0') {
        console.log(`${name}: [!] NOT DEPLOYED at ${cleanAddr}`);
        continue;
      }

      const token = await ethers.getContractAt('contracts/IERC20.sol:IERC20', cleanAddr);
      const bal = await token.balanceOf(TR);
      console.log(`${name}: ${ethers.formatUnits(bal, 18)} (At: ${cleanAddr})`);
    } catch (e) {
      console.log(`${name}: ERROR -> ${e.reason || e.message}`);
    }
  }
}
main().catch(console.error);