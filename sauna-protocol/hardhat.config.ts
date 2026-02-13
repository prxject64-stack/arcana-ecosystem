import { defineConfig, configVariable } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox-mocha-ethers";
import hardhatIgnition from "@nomicfoundation/hardhat-ignition-ethers";
import hardhatKeystore from "@nomicfoundation/hardhat-keystore";

export default defineConfig({
  // Hardhat 3 must see both plugins to resolve the task AND the secret
  plugins: [hardhatIgnition, hardhatKeystore],
  solidity: {
    version: "0.8.24",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200,
      },
    },
  },
  networks: {
    arcana: {
      type: "http",
      url: "http://127.0.0.1:8545",
      accounts: [configVariable("ARCANA_KEY")],
    },
  },
});
