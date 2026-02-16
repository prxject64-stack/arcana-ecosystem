import { ethers } from "ethers";
import fs from "fs";

async function main() {
  const RPC_URL = "http://127.0.0.1:8545";
  const PRIVATE_KEY = "0xfdfcd399e13c4f7e1612fd5e655159f899a4951ecf21d153a6adef68474271d2";

  const provider = new ethers.JsonRpcProvider(RPC_URL);
  const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

  const artifactPath = "./artifacts/contracts/SaunaPrivacyMask.sol/SaunaPrivacyMask.json";
  const artifact = JSON.parse(fs.readFileSync(artifactPath, "utf8"));

  const constructor = artifact.abi.find(x => x.type === "constructor");
  const argCount = constructor ? constructor.inputs.length : 0;

  console.log("--------------------------------------------------");
  console.log("Verified Signer:", wallet.address);
  console.log("Constructor Inputs Required:", argCount);

  const Factory = new ethers.ContractFactory(artifact.abi, artifact.bytecode, wallet);
  
  let contract;
  if (argCount === 0) {
    contract = await Factory.deploy();
  } else {
    console.log("Providing Signer Address as constructor argument...");
    contract = await Factory.deploy(wallet.address);
  }

  await contract.waitForDeployment();
  console.log("SUCCESS! Address:", await contract.getAddress());
  console.log("136B CC Liquidity Shield: ACTIVE");
  console.log("--------------------------------------------------");
}

main().catch(console.error);