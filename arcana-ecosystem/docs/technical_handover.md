# Obsidian Layer: Amazon Engineering Handover v1.0

## API Endpoint & Auth
- **Endpoint:** `https://node.arcana-ecosystem.io/v1/payout`
- **Auth:** Stateless HMAC-SHA256 with 52MB Merkle-Root Verification.
- **Protocol:** Sauna P2P v4.2

## Verification Logic
To achieve 4,500/s, utilize the sharded proof path:
`GET /vault/proof?shard=1&asset=CC`

## Stress Test Baseline
- **Verified Throughput:** 4,500 swaps/sec
- **Liquidity Depth:** 136B CC
- **Finality:** < 1000ms
