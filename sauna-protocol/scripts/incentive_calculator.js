const SUSD_PRICE = 0.8107;
const TARGET_INTAKE = 10000000; // 10M sUSD
const DE_PEG_LOSS = (1 - SUSD_PRICE) * TARGET_INTAKE;

console.log('--- WHALE RECOVERY CALCULATION ---');
console.log('Current sUSD Value: $' + SUSD_PRICE);
console.log('Whale Paper Loss: $' + DE_PEG_LOSS.toLocaleString());
console.log('Required ARC Bonus: ' + (DE_PEG_LOSS * 1.1).toLocaleString() + ' ARC');
console.log('Status: MINTING RECOVERY OFFER');
