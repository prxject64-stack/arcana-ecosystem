const { ethers } = require("hardhat");
async function main() {
  const ccpAddress = "YOUR_CC-P_CONTRACT_ADDRESS"; 
  const ccp = await ethers.getContractAt("IERC20", ccpAddress);
  const balance = await ccp.totalSupply();
  console.log("Verified Private Reserve: " + balance.toString() + " CC-P");
}
main();
