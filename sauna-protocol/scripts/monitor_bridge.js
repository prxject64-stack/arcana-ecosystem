const hre = require('hardhat');

async function main() {
  const bridgeAddress = '0x5FbDB2315678afecb367f032d93F642f64180aa3';
  console.log('--- MONITORING BRIDGE FOR WHALE INBOUNDS ---');
  console.log('Target: ' + bridgeAddress);

  hre.ethers.provider.on({ address: bridgeAddress }, (log) => {
    console.log('!!! ALERT: INCOMING INTERACTION DETECTED !!!');
    console.log('Transaction Hash: ' + log.transactionHash);
  });

  // Keep script running
  await new Promise(() => {});
}

main().catch((error) => { console.error(error); });
