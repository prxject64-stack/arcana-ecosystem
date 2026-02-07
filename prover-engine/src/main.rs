use std::{env, sync::Arc, time::Duration};
use tokio::time::sleep;
use ethers::prelude::*;

abigen!(IERC20, r#"[ 
    function transfer(address to, uint256 amount) external returns (bool)
]"#);

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let rpc_url = env::var("RPC_URL")?;
    let priv_key = env::var("PRIVATE_KEY")?.trim_start_matches("0x").to_string();
    let arc_vault: Address = "0xF0e11D2a5a9936AdCAc36724EB477465f64Dc8f4".parse()?;
    let cc_addr: Address = "0x8847E51E89A609D2D11Dc10020991A29D500ABf0".parse()?;
    
    let provider = Provider::<Http>::try_from(rpc_url)?;
    let chain_id = provider.get_chainid().await?;
    let wallet = priv_key.parse::<LocalWallet>()?.with_chain_id(chain_id.as_u64());
    let address = wallet.address();

    let client = SignerMiddleware::new(provider, wallet);
    let client = NonceManagerMiddleware::new(client, address);
    let client = Arc::new(client);
    
    let cc_token = IERC20::new(cc_addr, client.clone());

    println!("[ACTION] Moving CC to ARC Vault: {:?}", arc_vault);

    for i in 1..=4500 {
        loop {
            // Sending 1,000,000 CC per swap to fuel the ARC contract
            match cc_token.transfer(arc_vault, U256::from(1000000)).send().await {
                Ok(tx) => {
                    if i % 10 == 0 { println!("[SUCCESS] Swap {}: {:?}", i, *tx); }
                    break;
                }
                Err(e) => {
                    println!("[RETRY] Swap {} failed: {}. Syncing nonce...", i, e);
                    // FIXED: Correct method name and argument
                    client.initialize_nonce(None).await?; 
                    sleep(Duration::from_secs(2)).await;
                }
            }
        }
    }
    println!("[SUCCESS] Sovereign sequence complete.");
    Ok(())
}
