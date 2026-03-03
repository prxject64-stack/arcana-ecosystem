import '@nomicfoundation/hardhat-toolbox';

export default {
  solidity: {
    version: '0.8.24',
    settings: {
      optimizer: {
        enabled: true,
        runs: 200,
      },
      viaIR: true,
    },
  },
  networks: {
    localhost: {
      url: 'http://127.0.0.1:8545',
      gas: 2100000,
      gasPrice: 0,
    }
  }
};