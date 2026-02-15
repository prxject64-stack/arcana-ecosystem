import hre from "hardhat";

async function main() {
  const ethers = hre.ethers;
  const [deployer] = await ethers.getSigners();

  console.log("--------------------------------------------------");
  console.log("Verified Signer:", deployer.address);
  console.log("Deploying SaunaPrivacyMask...");

  const Factory = await ethers.getContractFactory("SaunaPrivacyMask");
  const contract = await Factory.deploy();

  await contract.waitForDeployment();
  const address = await contract.getAddress();

  console.log("SUCCESS! Address:", address);
  console.log("--------------------------------------------------");
}

main().catch((e) => { console.error(e); process.exit(1); });