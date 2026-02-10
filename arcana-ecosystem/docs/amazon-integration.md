# Obsidian Layer: Amazon SP-API Integration Guide (v2026.1)

## Overview
This document outlines the technical requirements for Amazon Treasury to interface with the Obsidian Layer Settlement Node for T-0 Global Seller Payouts.

## Connectivity
- **Endpoint:** `https://node.arcana.obsidian/v1/settle`
- **Protocol:** ISO-20022 (pacs.008.001.08)
- **Authentication:** mTLS + sec-sys hardware signing

## Endpoint: POST /payout/instant
Facilitates immediate liquidity release from the 136B CC pool.

### Request Schema
| Field | Type | Description |
| :--- | :--- | :--- |
| payout_id | UUID | Unique Amazon transaction ID |
| amount_cc | Integer | Value in Credit Coin (CC) |
| destination | String | Seller Wallet Address (Arcana Standard) |

### Response
- **Status:** 200 OK
- **Latency:** < 500ms
- **Finality:** Mathematical (Immutable)
