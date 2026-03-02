import { ethers } from "ethers";
import fs from "fs";

async function main() {
  const provider = new ethers.JsonRpcProvider("http://127.0.0.1:8545");
  const signer = await provider.getSigner("0x218e8c79F8a12472a4bA48dd76B55A3e39e40cc8");
  const saUSDAddress = "0x4AC1B117e2713a1d8C5A3aCa5B8EfEA139b99640";

  console.log("Deploying SaunaVault linked to saUSD...");

  const artifactPath = "./artifacts/contracts/SaunaVault.sol/SaunaVault.json";
  if (!fs.existsSync(artifactPath)) {
    throw new Error("Artifact not found. Run 'npx hardhat compile' first.");
  }

  const artifact = JSON.parse(fs.readFileSync(artifactPath, "utf8"));
  const factory = new ethers.ContractFactory(artifact.abi, artifact.bytecode, signer);
  
  const vault = await factory.deploy(saUSDAddress);
  await vault.waitForDeployment();

  const vaultAddress = await vault.getAddress();
  console.log("-----------------------------------------------");
  console.log("SaunaVault successfully deployed!");
  console.log("Vault Address:", vaultAddress);
  console.log("Linked saUSD:", saUSDAddress);
  console.log("-----------------------------------------------");
}

main().catch((error) => {
  console.error("Vault Deployment Failed:", error);
  process.exit(1);
});