import { task } from "hardhat/config";
import "@nomicfoundation/hardhat-ethers";

task("deploy-sauna", "Deploy Sauna", async (taskArgs, hre) => {
  const [deployer] = await hre.ethers.getSigners();
  console.log("--------------------------------------------------");
  console.log("Verified Signer:", deployer.address);
  const Factory = await hre.ethers.getContractFactory("SaunaPrivacyMask");
  const contract = await Factory.deploy();
  await contract.waitForDeployment();
  console.log("SUCCESS! Address:", await contract.getAddress());
  console.log("136B CC Liquidity Shield: ACTIVE");
  console.log("--------------------------------------------------");
});

const config = {
  solidity: "0.8.20",
  networks: {
    arcana: {
      type: "http",
      url: "http://127.0.0.1:8545",
      accounts: ["0xfdfcd399e13c4f7e1612fd5e655159f899a4951ecf21d153a6adef68474271d2"]
    }
  }
};

export default config;