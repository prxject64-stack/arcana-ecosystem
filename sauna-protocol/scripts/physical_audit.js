async function main() {
  const TR = '0x322813fd9a05da47206818293028c39ed8b00000';
  const CC = '0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512';
  
  const code = await ethers.provider.getCode(CC);
  console.log('--- SOVEREIGN PHYSICAL LAYER CHECK ---');
  console.log('Bytecode length at CC address:', code.length);
  
  if (code.length <= 2) {
    console.log('CRITICAL: No code found at address. Resurrection failed.');
    return;
  }

  const balanceData = '0x70a08231' + TR.substring(2).padStart(64, '0');
  const result = await ethers.provider.send('eth_call', [{ to: CC, data: balanceData }, 'latest']);
  console.log('Raw Balance Data:', result);
  console.log('Sovereign CC Balance:', ethers.formatUnits(result, 18), 'CC');
}
main().catch(console.error);