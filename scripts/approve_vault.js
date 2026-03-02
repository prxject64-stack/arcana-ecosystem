import { ethers } from "ethers";

async function main() {
  const provider = new ethers.JsonRpcProvider("http://127.0.0.1:8545");
  const signer = await provider.getSigner("0x218e8c79F8a12472a4bA48dd76B55A3e39e40cc8");
  const saUSDAddress = "0x4AC1B117e2713a1d8C5A3aCa5B8EfEA139b99640";
  const vaultAddress = "0x1791E91733E32eDFd2f98ff772a64335EE3E2d0D";

  const abi = ["function approve(address spender, uint256 amount) public returns (bool)"];
  const saUSD = new ethers.Contract(saUSDAddress, abi, signer);

  const amount = ethers.parseUnits("1000000", 18);
  console.log("Approving Vault for 1M saUSD...");
  const tx = await saUSD.approve(vaultAddress, amount);
  await tx.wait();

  console.log("-----------------------------------------------");
  console.log("Approval Confirmed!");
  console.log("TX Hash:", tx.hash);
  console.log("-----------------------------------------------");
}

main().catch(console.error);