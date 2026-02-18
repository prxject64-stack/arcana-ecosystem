import "@nomicfoundation/hardhat-toolbox";

export default {
  solidity: {
    compilers: [
      { version: "0.8.28" },
      { version: "0.8.20" },
      { version: "0.8.19" },
      { version: "0.7.6" },
      { version: "0.6.12" },
      { version: "0.5.16" }
    ],
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  },
  networks: {
    arcana: {
      url: process.env.ARCANA_RPC_URL || "http://127.0.0.1:8547",
      accounts: process.env.PEER2_PRIVATE_KEY ? [process.env.PEER2_PRIVATE_KEY] : [],
    }
  }
};
