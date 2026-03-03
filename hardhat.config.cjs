require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  solidity: "0.8.20",
  networks: {
    arcana: {
      url: "http://127.0.0.1:8545",
      accounts: ["0x218e8c79f8a12472a4ba48dd76b55a3e39e40cc8"], // Use your actual private key here if deploying via Hardhat
    },
  },
};
