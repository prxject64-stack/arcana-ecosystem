async function main() {
  const TR = '0x322813fd9a05da47206818293028c39ed8b00000';
  const ASSETS = {
    'CC': '0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512',
    'sUSD': '0x57Ab1ec1520597403985d084E5a812D34E982F0E',
    'ARC': '0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9'
  };

  console.log('--- SOVEREIGN ECOSYSTEM AUDIT ---');
  for (const [name, addr] of Object.entries(ASSETS)) {
    try {
      const token = await ethers.getContractAt('contracts/IERC20.sol:IERC20', addr);
      const bal = await token.balanceOf(TR);
      console.log(`${name}: ${ethers.formatUnits(bal, 18)}`);
    } catch (e) {
      console.log(`${name}: NOT_FOUND (Check Address/Genesis)`);
    }
  }
}
main().catch(console.error);