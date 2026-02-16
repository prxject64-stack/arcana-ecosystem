import hre from "hardhat";
import "@nomicfoundation/hardhat-ethers";

async function main() {
  // Manual injection check for Hardhat 3 ESM bug
  if (!hre.ethers) {
    console.log("Bug Detected: HRE Ethers not found. Re-initializing...");
  }

  const [deployer] = await hre.ethers.getSigners();
  console.log("--------------------------------------------------");
  console.log("Verified Signer:", deployer.address);

  const Factory = await hre.ethers.getContractFactory("SaunaPrivacyMask");
  const contract = await Factory.deploy();
  await contract.waitForDeployment();

  const address = await contract.getAddress();
  console.log("SUCCESS! Sauna Mask Address:", address);
  console.log("136B CC Liquidity Shield: ACTIVE");
  console.log("--------------------------------------------------");
}

main().catch((error) => {
  console.error("Critical Deployment Failure:", error);
  process.exit(1);
});