# Technical FAQ: Arcana Obsidian Layer (136B CC)

### 1. How is the 136B CC liquidity secured?
The vault is locked via a **Multi-Signature Sharded Merkle Root**. No single node can move the liquidity. 136B CC is cross-referenced across 4,500 simultaneous peer-to-peer swaps to ensure zero double-spending.

### 2. What is the 'Sauna Protocol's' role in high-velocity swaps?
The Sauna Protocol manages "State Pruning." It allows the node to maintain 4,500/s throughput by keeping the active ledger sharded and "hot," while archiving settled swaps into the "cold" 52MB Merkle tree.

### 3. What is the 'Stateless Verification' advantage?
Amazon gates do not need to download the entire blockchain. They use Merkle Proofs (approx. 842 Bytes) to verify any transaction in sub-millisecond timeframes.

### 4. Handling Network Latency
The system utilizes a "T-0" settlement logic. If a network partition occurs, the **Obsidian Sentinel** automatically throttles the gate to 500/s to prevent liquidity leakage until parity is restored.
