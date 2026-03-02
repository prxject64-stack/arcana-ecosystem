import { ethers } from "ethers";

async function main() {
  const provider = new ethers.JsonRpcProvider("http://127.0.0.1:8545");
  const signer = await provider.getSigner("0x218e8c79F8a12472a4bA48dd76B55A3e39e40cc8");
  const vaultAddress = "0x1791E91733E32eDFd2f98ff772a64335EE3E2d0D";

  const abi = ["function deposit(uint256 amount) external"];
  const vault = new ethers.Contract(vaultAddress, abi, signer);

  const amount = ethers.parseUnits("1000000", 18);
  console.log("Depositing 1,000,000 saUSD into the Vault...");
  const tx = await vault.deposit(amount);
  await tx.wait();

  console.log("-----------------------------------------------");
  console.log("Deposit Successful!");
  console.log("TX Hash:", tx.hash);
  console.log("-----------------------------------------------");
}

main().catch(console.error);