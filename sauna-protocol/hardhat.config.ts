import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox-mocha-ethers";

const config: HardhatUserConfig = {
  solidity: "0.8.20",
  networks: {
    arcana: {
      type: "http", // This is the missing discriminator required by Hardhat 3
      url: "http://127.0.0.1:8545",
      accounts: ["0xYOUR_VAULT_PRIVATE_KEY"], 
    }
  }
};

export default config;
