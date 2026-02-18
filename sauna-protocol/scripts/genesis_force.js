async function main() {
  const CC_ADDR = '0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512';
  const TR = '0x322813fd9a05da47206818293028c39ed8b00000';
  
  // 1. Force-deploy the Bytecode to the address
  const artifact = await artifacts.readArtifact('contracts/IERC20.sol:IERC20');
  await network.provider.send('hardhat_setCode', [CC_ADDR, artifact.deployedBytecode]);
  
  // 2. Mint the 146B CC to the Treasury
  // Note: Since this is a raw IERC20, we use hardhat_setStorageAt to manually force the balance
  const balanceSlot = ethers.keccak256(ethers.AbiCoder.defaultAbiCoder().encode(['address', 'uint256'], [TR, 0]));
  await network.provider.send('hardhat_setStorageAt', [
    CC_ADDR,
    balanceSlot,
    ethers.toBeHex(ethers.parseUnits('146000000000', 18), 32)
  ]);

  console.log('GENESIS COMPLETE: 146B CC Force-Injected at', CC_ADDR);
}
main().catch(console.error);