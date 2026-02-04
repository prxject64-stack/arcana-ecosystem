use ethers::prelude::*;
use ethers::types::transaction::eip2718::TypedTransaction; // THE MISSING IMPORT
use eyre::Result;
use std::sync::Arc;
use std::env;

#[tokio::main]
async fn main() -> Result<()> {
    let rpc_url = env::var("RPC_URL").map_err(|_| eyre::eyre!("Missing RPC_URL"))?;
    let priv_key = env::var("PRIVATE_KEY").map_err(|_| eyre::eyre!("Missing PRIVATE_KEY"))?;
    
    let provider = Provider::<Http>::try_from(rpc_url)?;
    let chain_id = provider.get_chainid().await?;
    let wallet: LocalWallet = priv_key.parse::<LocalWallet>()?.with_chain_id(chain_id.as_u64());
    let client = Arc::new(SignerMiddleware::new(provider, wallet.clone()));

    // Get current network fees with safety buffer
    let block = client.get_block(BlockNumber::Latest).await?.unwrap();
    let base_fee = block.base_fee_per_gas.unwrap_or(U256::from(20_000_000u64));
    let max_fee = (base_fee * 130) / 100; // 30% buffer for 2026 volatility
    let priority_fee = U256::from(100_000u64); 

    let args: Vec<String> = env::args().collect();
    let is_broadcast = args.contains(&"--broadcast".to_string());

    if args.contains(&"--auth-sovereign".to_string()) {
        println!("--- [VAULT DEPLOYMENT: TYPE 2] ---");
        if is_broadcast {
            let mut tx = Eip1559TransactionRequest::new()
                .to(wallet.address())
                .value(0)
                .max_fee_per_gas(max_fee)
                .max_priority_fee_per_gas(priority_fee);
            
            tx.chain_id = Some(chain_id.as_u64().into());

            let typed_tx: TypedTransaction = tx.into();
            
            let pending = client.send_transaction(typed_tx, None).await?;
            println!("Broadcast Success! Hash: {:?}", pending.tx_hash());
            
            // Wait for confirmation
            let receipt = pending.await?.ok_or_else(|| eyre::eyre!("TX Dropped"))?;
            println!("Status: Confirmed in block {}", receipt.block_number.unwrap());
        } else {
            println!("(Simulation) Would deploy vault with max_fee: {}", max_fee);
        }
    }
    Ok(())
}
