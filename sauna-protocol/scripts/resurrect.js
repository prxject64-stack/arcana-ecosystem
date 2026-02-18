async function main() {
  const networkName = network.name;
  if (networkName !== 'localhost') {
    console.log('CRITICAL ERROR: Script is running on "' + networkName + '". USE --network localhost');
    process.exit(1);
  }

  const TR = '0x322813fd9a05da47206818293028c39ed8b00000';
  const ASSETS = {
    'CC': '0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512',
    'sUSD': '0x57Ab1ec1520597403985d084E5a812D34E982F0E',
    'ARC': '0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9'
  };

  const artifact = await artifacts.readArtifact('contracts/IERC20.sol:IERC20');

  console.log('--- FORCING SOVEREIGN STATE TO PERSISTENT NODE ---');
  for (const [name, addr] of Object.entries(ASSETS)) {
    await network.provider.send('hardhat_setCode', [addr, artifact.deployedBytecode]);
    
    // Manual storage slot injection for balance
    const balanceSlot = ethers.keccak256(ethers.AbiCoder.defaultAbiCoder().encode(['address', 'uint256'], [TR, 0]));
    await network.provider.send('hardhat_setStorageAt', [
      addr,
      balanceSlot,
      ethers.toBeHex(ethers.parseUnits('146000000000', 18), 32)
    ]);
    
    // IMMEDIATE VERIFICATION WITHIN SAME PROCESS
    const check = await ethers.provider.getCode(addr);
    console.log(`[+] ${name} verified at ${addr}. Bytecode length: ${check.length}`);
  }
}
main().catch(console.error);