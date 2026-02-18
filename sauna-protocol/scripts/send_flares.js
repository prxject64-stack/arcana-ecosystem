const hre = require("hardhat");

async function main() {
  const [owner] = await hre.ethers.getSigners();
  const rawTargets = [
    { name: "Aave_Collector", addr: "0x1f84a51296691320478c98b8d77f2bbd17d34350" },
    { name: "Kwenta_Treasury", addr: "0x920C107773f32420958930799797A699456b" },
    { name: "Curve_Whale", addr: "0x8ad525046270b200b6526131b7f03673c68383e9" }
  ];

  const hexMsg = "0x" + Buffer.from("EXIT sUSD TRAP. 1:1 BRIDGE LIVE AT 0x5FbDB2315678afecb367f032d93F642f64180aa3. 1B CC-P BACKED. - ARCANA").toString("hex");

  for (const whale of rawTargets) {
    try {
      const validAddr = hre.ethers.getAddress(whale.addr.trim());
      console.log("--- SENDING FLARE TO " + whale.name + " (" + validAddr + ") ---");
      const tx = await owner.sendTransaction({
        to: validAddr,
        value: hre.ethers.parseUnits("0.0001", "ether"),
        data: hexMsg
      });
      console.log("[SUCCESS] " + whale.name + " | TX: " + tx.hash);
    } catch (e) {
      console.error("[FAILED] Could not send to " + whale.name + ": " + e.message);
    }
  }
}

main().catch((error) => { console.error(error); process.exitCode = 1; });
