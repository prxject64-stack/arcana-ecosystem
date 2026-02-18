import "@nomicfoundation/hardhat-toolbox";

export default {
  solidity: "0.8.20",
  networks: {
    arcana: {
      url: "http://127.0.0.1:8547",
      accounts: process.env.PEER2_PRIVATE_KEY ? [process.env.PEER2_PRIVATE_KEY] : [],
    }
  }
};
