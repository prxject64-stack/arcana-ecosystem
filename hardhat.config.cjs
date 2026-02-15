const { task } = require("hardhat/config");
require("@nomicfoundation/hardhat-ethers");

module.exports = {
  solidity: {
    version: "0.8.20",
    settings: {
      evmVersion: "paris",
      optimizer: { enabled: true, runs: 200 }
    }
  },
  networks: {
    arcana: {
      type: "http",
      url: "http://127.0.0.1:8545",
      accounts: ["0xfdfcd399e13c4f7e1612fd5e655159f899a4951ecf21d153a6adef68474271d2"]
    }
  }
};