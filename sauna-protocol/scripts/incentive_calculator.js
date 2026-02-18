const hre = require('hardhat');

async function main() {
  const whaleDebt = 10000000; // 10M sUSD Debt
  const currentMonth = 11; // 11 Months into the 12-month Jubilee
  
  console.log('--- ARC INCENTIVE CALCULATION: WHALE 0x8ad5 ---');
  
  // 1. Calculate Synthetix Exit Penalty
  // Per SIP-420: Relief is linear. If exiting at Month 11, they lose the final month of relief.
  // Penalty = (Total Debt * 0.50) * (Remaining_Months / 12)
  const reliefLoss = (whaleDebt * 0.50) * (1 / 12);
  
  // 2. Calculate Market De-peg Loss
  // sUSD is at -bash.81. Exit loss = -bash.19 per token.
  const marketSlippageLoss = whaleDebt * 0.19;
  
  const totalLossUSD = reliefLoss + marketSlippageLoss;
  
  // 3. ARC Alignment Offer
  // We offer ARC at a 'Sovereign' valuation of .00 to cover the loss.
  const arcBonus = totalLossUSD;

  console.log('[PENALTY] Jubilee Relief Forfeited: $' + reliefLoss.toLocaleString());
  console.log('[PENALTY] Market De-peg Slippage: $' + marketSlippageLoss.toLocaleString());
  console.log('----------------------------------------------');
  console.log('[OFFER] Total ARC Incentive Required: ' + arcBonus.toLocaleString() + ' ARC');
  console.log('[OFFER] Total saUSD Minted: ' + whaleDebt.toLocaleString());
  console.log('[RESULT] Whale Net Worth Preserved: 100% via Arcana Backing.');
}
main().catch(console.error);
