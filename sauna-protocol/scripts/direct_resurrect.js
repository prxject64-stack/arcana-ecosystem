const { ethers } = require('ethers');
const fs = require('fs');
async function main() {
  const provider = new ethers.JsonRpcProvider('http://127.0.0.1:8545');
  const TR = '0x322813fd9a05da47206818293028c39ed8b00000'.toLowerCase();
  const ASSETS = { 'CC-P': '0xe7f1725e7734ce288f8367e1bb143e90bb3f0512', 'saUSD': '0x57ab1ec1520597403985d084e5a812d34e982f0e', 'ARC-S': '0xcf7ed3acca5a467e9e704c703e8d87f634fb0fc9' };
  const artifact = JSON.parse(fs.readFileSync('artifacts/contracts/SovereignToken.sol/SovereignToken.json', 'utf8'));
  for (const [name, addr] of Object.entries(ASSETS)) {
    await provider.send('hardhat_setCode', [addr, artifact.deployedBytecode]);
    const slot = ethers.keccak256(ethers.AbiCoder.defaultAbiCoder().encode(['address', 'uint256'], [TR, 0]));
    const val = ethers.toBeHex(ethers.parseUnits('146000000000', 18), 32);
    await provider.send('hardhat_setStorageAt', [addr, slot, val]);
    const code = await provider.getCode(addr);
    console.log('[+] ' + name + ' Status: ' + (code.length > 2 ? 'SUCCESS' : 'FAILED'));
  }
}
main().catch(console.error);
