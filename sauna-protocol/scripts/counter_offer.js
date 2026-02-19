const WHALES = ["Whale 3", "Whale 4", "Whale 5"];
const OFFER_TEXT = `OFFICIAL NOTICE: Arcana Sovereign (Damarieus Jones) offers a 1:1 Rescue for your distressed sUSD positions. Avoid the 19% Curve slippage. Swap for ARC today.`;

WHALES.forEach(whale => {
    console.log(`GENERING OFFER FOR ${whale}...`);
    console.log(`MESSAGE: ${OFFER_TEXT}`);
});
