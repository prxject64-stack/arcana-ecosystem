const targets = [
  { address: "0x8ad520258f8853344581a3...", balance: 10450000, label: "Aave Whale 0x8ad5" },
  { address: "0xCA8Fa8f0b631EcdB18Cda619C4Fc9d197c8aFfCa", balance: 5200000, label: "Synthetix OG" },
  { address: "0xE92d1A43df510F82C66382592a047d288f85226f", balance: 3100000, label: "Distressed Fund" }
];

const SUSD_PRICE = 0.8107;
console.log("--- ARCANA SOVEREIGN: TARGETED AIR-STRIKE LIST ---");
targets.forEach(w => {
    let paper_loss = w.balance * (1 - SUSD_PRICE);
    let cliff_loss = w.balance * 0.125; // First month burn
    console.log(`\nTARGET: ${w.label} (${w.address})`);
    console.log(`Current Paper Loss: $${paper_loss.toLocaleString()}`);
    console.log(`APRIL 30 BURN RISK: $${cliff_loss.toLocaleString()} (MONTHLY)`);
    console.log(`STATUS: SENDING MANIFESTO VIA DE-BANK/DISCORD...`);
});
