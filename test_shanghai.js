import pkg from 'hardhat';
const { ethers } = pkg;

async function main() {
  const [signer] = await ethers.getSigners();
  console.log('Testing PUSH0 on:', signer.address);

  const rawTx = {
    to: '0x0000000000000000000000000000000000000000',
    data: '0x5f',
    gasLimit: 30000
  };

  try {
    const tx = await signer.sendTransaction(rawTx);
    await tx.wait();
    console.log('SUCCESS: PUSH0 is supported. Shanghai is ACTIVE.');
  } catch (e) {
    console.log('FAILURE: Invalid Opcode. Shanghai is DISABLED.');
  }
}

main().catch(console.error);