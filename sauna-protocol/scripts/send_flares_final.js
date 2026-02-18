const hre = require("hardhat");

async function main() {
  const [owner] = await hre.ethers.getSigners();
  const rawTargets = [
    { name: "Kwenta_Treasury", addr: "0x920Cf626a271321C151D027030D5d08aF699456b" }
  ];

  const hexMsg = "0x" + Buffer.from("EXIT sUSD TRAP. 1:1 BRIDGE LIVE AT 0x5FbDB2315678afecb367f032d93F642f64180aa3. 1B CC-P BACKED. - ARCANA").toString("hex");

  for (const whale of rawTargets) {
    try {
      const validAddr = hre.ethers.getAddress(whale.addr.trim());
      console.log("--- SENDING REMAINING FLARE TO " + whale.name + " ---");
      const tx = await owner.sendTransaction({
        to: validAddr,
        value: hre.ethers.parseUnits("0.0001", "ether"),
        data: hexMsg
      });
      console.log("[SUCCESS] " + whale.name + " | TX: " + tx.hash);
    } catch (e) {
      console.error("[FAILED] " + whale.name + ": " + e.message);
    }
  }
}

main().catch((error) => { console.error(error); process.exitCode = 1; });
