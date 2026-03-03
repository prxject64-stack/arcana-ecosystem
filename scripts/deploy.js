import { ethers } from "ethers";
import fs from "fs";

async function main() {
  // 1. Manually connect to your Sovereign Node (Geth)
  const provider = new ethers.JsonRpcProvider("http://127.0.0.1:8545");
  
  // 2. Access your unlocked Sovereign Account
  // Ethers v6 requires the address or index for getSigner on a JSON-RPC node
  const signer = await provider.getSigner("0x218e8c79f8a12472a4ba48dd76b55a3e39e40cc8");

  console.log("Deploying saUSD with Sovereign Account:", signer.address);

  // 3. Load the Bytecode and ABI directly from your artifacts
  const artifactPath = "./artifacts/contracts/SaunaUSD.sol/SaunaUSD.json";
  if (!fs.existsSync(artifactPath)) {
    throw new Error("Artifact not found. Run 'npx hardhat compile' first.");
  }
  const artifact = JSON.parse(fs.readFileSync(artifactPath, "utf8"));

  // 4. Create the Deployment Factory
  const factory = new ethers.ContractFactory(artifact.abi, artifact.bytecode, signer);
  
  console.log("Submitting transaction to the Sovereign Chain...");
  const contract = await factory.deploy();
  
  console.log("Waiting for block confirmation...");
  await contract.waitForDeployment();

  const address = await contract.getAddress();
  console.log("-----------------------------------------------");
  console.log("Sauna USD (saUSD) successfully deployed!");
  console.log("Contract Address:", address);
  console.log("Sovereign Supply: 1,000,000,000 saUSD");
  console.log("-----------------------------------------------");
}

main().catch((error) => {
  console.error("Critical Deployment Failure:", error);
  process.exit(1);
});
