async function main() {
  const TR = '0x322813fd9a05da47206818293028c39ed8b00000'.toLowerCase();
  
  // Addresses normalized to lowercase to kill checksum errors
  const ASSETS = {
    'CC': '0xe7f1725e7734ce288f8367e1bb143e90bb3f0512',
    'sUSD': '0x57ab1ec1520597403985d084e5a812d34e982f0e',
    'ARC': '0xcf7ed3acca5a467e9e704c703e8d87f634fb0fc9'
  };

  const artifact = await artifacts.readArtifact('contracts/IERC20.sol:IERC20');
  const bytecode = artifact.deployedBytecode;

  console.log('--- EXECUTING SOVEREIGN OVERRIDE ---');

  for (const [name, addr] of Object.entries(ASSETS)) {
    // Force lowercase to ensure no checksum drama
    const target = addr.toLowerCase();

    // 1. Inject Code
    await network.provider.send('hardhat_setCode', [target, bytecode]);
    
    // 2. Inject Balance (Slot 0)
    const balanceSlot = ethers.keccak256(ethers.AbiCoder.defaultAbiCoder().encode(['address', 'uint256'], [TR, 0]));
    await network.provider.send('hardhat_setStorageAt', [
      target,
      balanceSlot,
      ethers.toBeHex(ethers.parseUnits('146000000000', 18), 32)
    ]);
    
    // 3. Verification
    const code = await ethers.provider.getCode(target);
    console.log(`[+] ${name} Status: ${code.length > 2 ? 'DEPLOYED' : 'FAILED'} (Length: ${code.length})`);
  }
}
main().catch(console.error);