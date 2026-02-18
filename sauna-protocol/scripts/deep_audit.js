async function main() {
  const TR = '0x322813fd9a05da47206818293028c39ed8b00000';
  const ASSETS = {
    'CC (Credit Coin)': '0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512',
    'sUSD (Synthetix)': '0x57Ab1ec1520597403985d084E5a812D34E982F0E',
    'ARC (Arcana)': '0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9'
  };

  console.log('--- SOVEREIGN ECOSYSTEM AUDIT (DEEP SCAN) ---');
  for (const [name, addr] of Object.entries(ASSETS)) {
    try {
      // Use the generic IERC20 interface artifact from your local build
      const token = await ethers.getContractAt('contracts/IERC20.sol:IERC20', addr);
      const bal = await token.balanceOf(TR);
      const code = await ethers.provider.getCode(addr);
      
      if (code === '0x') {
         console.log(`${name}: EMPTY_ADDRESS (No contract deployed here)`);
      } else {
         console.log(`${name}: ${ethers.formatUnits(bal, 18)}`);
      }
    } catch (e) {
      console.log(`${name}: SCAN_ERROR (${e.message.substring(0, 50)}...)`);
    }
  }
}
main().catch(console.error);