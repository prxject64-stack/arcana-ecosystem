const hre = require("hardhat");

async function main() {
  const CC_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3";
  const cc = await hre.ethers.getContractAt("CreditCoinPrivate", CC_ADDRESS);

  const name = await cc.name();
  const symbol = await cc.symbol();
  const rawSupply = await cc.totalSupply();
  const decimals = await cc.decimals();
  
  // Format for 136B
  const formattedSupply = hre.ethers.formatUnits(rawSupply, decimals);

  console.log("--------------------------------------------------");
  console.log("ARCANA ECOSYSTEM VERIFICATION");
  console.log("Token:", name, "(" + symbol + ")");
  console.log("Total Supply:", formattedSupply, "CC");
  console.log("Status:", formattedSupply === "136000000000.0" ? "VERIFIED" : "MISMATCH");
  console.log("--------------------------------------------------");
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
