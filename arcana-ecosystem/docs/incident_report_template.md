# Incident Report: Obsidian Layer Throughput Regulation

**Status:** [RESOLVED / MONITORING]
**Incident ID:** ARC-AMZ-2026-001
**Timestamp:** [INSERT DATE/TIME]

## Executive Summary
At [TIME], the Obsidian Sentinel detected a throughput spike of [X,XXX] TPS, exceeding the agreed-upon SLA limit of 4,500/s. To protect the 136B CC vault integrity, the Autonomous Circuit Breaker engaged a "Soft Throttle."

## Technical Root Cause
- **Trigger:** Throughput exceeded 4,500/s.
- **Action Taken:** Automated execution of `emergency_throttle.sh`.
- **System Impact:** Capacity reduced to 500/s; Latency increased to ~1200ms.

## Resolution
- [ ] Throughput normalized.
- [ ] Manual override executed: `miner --provision-gate --limit 4500`.
- [ ] Merkle-Root integrity verified (136B CC confirmed).

## Prevention
The Sauna Protocol is being tuned to handle this specific traffic pattern without triggering a hard throttle in the future.
