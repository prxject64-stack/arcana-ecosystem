import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox-mocha-ethers";

const config: HardhatUserConfig = {
  solidity: "0.8.20",
  networks: {
    arcana: {
      url: "http://127.0.0.1:8545",
      // Use your Vault address private key here
      accounts: ["0x995c7b87a714f4a018af1a3542af6463a4d8c1744a9155127a234fee3be55a49"], 
      gasPrice: 1000000000, // 1 Gwei
    }
  }
};

export default config;
