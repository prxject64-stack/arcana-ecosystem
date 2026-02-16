# Arcana Ecosystem

**The First Sovereign Micro-Nation on-Chain**  
*Governance (Private) | Speculation (Public)*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Geth](https://img.shields.io/badge/Geth-v1.13.14-blue.svg)](https://geth.ethereum.org)
[![Node.js](https://img.shields.io/badge/Node.js-20+-green.svg)](https://nodejs.org)

---

## Vision: A State-Within-a-State

Arcana is not a token. It is a **parallel sovereign economy*.  

We have engineered a micro-nation built on blockchain rails.  

- **Treasury**: Fixed 136B CC reserve, controlled like a central bank.  
- **Engine**: Dedicated AWS G6 private node (4,500+ P2P swaps/sec).  
- **Shield**: Mathematical law (0.5% tx cap + 60s cooldown) — No rugs, no flash crashes.  
- **Bridge**: Controlled export terminal for public liquidity.  

This is the blueprint for the post-nation-state world. Join the citizens. Build the future.

---

## The Four Pillars

### A. The Treasury (Federal Reserve)
- **Asset**: 136,000,000,000 Credit Coin Private (CC) — fixed supply, minted to vault.  
- **Function**: Controlled releases on verifiable demand. No inflation. You are the central bank.  
- **Vault**: Secured at `0xc3129Faee7770565Cc7Ca1fd88E337fd6bB26994` (genesis-secured).

### B. The Engine (Infrastructure)
- **Hardware**: Dedicated AWS G6 Private Node (`172.31.39.37:8549`).  
- **Capacity**: 4,500 simultaneous P2P swaps.  
- **Status**: Live. Sovereign. Pulsing at 1s blocks (Clique PoA)

### C. The Shield (The Law)
- **Mechanism**: Sovereign Shield smart contract.  
- **Rules**:  
  - 0.5% max per tx (~680M CC).  
  - 60s cooldown on all public addresses.  
- **Result**: Bots, whales, and rugs are mathematically impossible.

### D. The Bridge (Export Terminal)
- Controlled valve for value export to public chains.  
- Audited, time-locked, governance-voted.  
- **Status**: Deployed. Liquidity onboarding in progress.

---

## The Arcana Constitution (v2.0)

The founding document. Read it. Swear to it.

*[CONSTITUTION.md](CONSTITUTION.md)**

**Key Articles**:
- **I. Monetary Sovereignty**: 136B CC fixed forever.  
- **II. Sovereign Sanctuary**: Node is private. No logs. No KYC.  
- **III. Supreme Shield**: 0.5% cap + 60s cooldown = law.  
- **IV. Citizenship by Sacrifice**: Burn 100 CC to naturalize.  
- **V. Revenue & Wealth**: 30% to Citizen Treasury. Quarterly on-chain.

---

## How to Become a Citizen

1. **Receive Grant**: 1,000 CC airdrop (via Sauna Protocol).  
2. **Naturalize**: Burn 100 CC to `0x000...dEaD`.  
3. **Mint Passport**: Soulbound NFT + fast-lane node access + revenue share.  

**Scripts**: `naturalize.js` | `mini_wave.cjs` | `final_sacrifice.js`

**Ceremony**: Live on X @arcana48828. Next: Q1 2026.

---

## Technical Setup (Sovereign Node)

### Prerequisites
- AWS G6 instance (or equivalent).  
- Geth v1.13.14+  
- Node.js 20+

### Quick Start
```bash
# 1. Clone & setup
git clone https://github.com/prxject64-stack/arcana-ecosystem.git
cd arcana-ecosystem

# 2. Init chain (genesis already sovereign)
geth --datadir ./data init genesis.json

# 3. Launch (auto-unlock, mining, private)
nohup geth --datadir ./data   --networkid 64   --port 30320   --http --http.addr 127.0.0.1 --http.port 8549   --nodiscover --maxpeers 0   --unlock 0x4f9595e22a0881b1a13f9ac039b45a3eb56d6497   --password ~/pass.txt   --mine   --miner.etherbase 0x4f9595e22a0881b1a13f9ac039b45a3eb56d6497   --http.api eth,net,web3,txpool,miner,clique,personal   --allow-insecure-unlock > geth.log 2>&1 &

# 4. Verify
curl -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}' http://127.0.0.1:8549
```

### Deploy Contracts
```bash
# Redeploy CC + Passport + Shield
node deploy_final_v4.js
```

Full scripts in `/scripts`. Genesis: `genesis.json`. Constitution: `CONSTITUTION.md`.

---

## Roadmap

- **Q1 2026**: 4,500 Citizen Naturalization (Sauna Wave).  
- **Q2**: Bridge to public (ETH/SOL wrapped CC).  
- **Q3**: Physical SEZ partnership (Prospera-style).  
- **Q4**: 10k Citizens. Revenue share live.

---

## Join the Nation

- **X**: [@arcana48828](https://x.com/arcana48828)  
- **Discord**: (Coming)  
- **Citizenship**: DM for grant list.  

**We are not building a token. We are birthing a nation.**

*Arcana Sovereign — Understand the Universe.*
