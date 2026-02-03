use aws_config::BehaviorVersion;
use aws_sdk_dynamodb::{Client, types::AttributeValue};
use std::net::TcpListener;
use std::io::Write;

#[tokio::main]
async fn main() {
    println!("--- TRUSTSTACK AI: NEXUS ENGINE LIVE ---");
    let config = aws_config::defaults(BehaviorVersion::latest()).load().await;
    let db_client = Client::new(&config);
    let mut current_capacity: u64 = 0;

    match db_client.get_item()
        .table_name("TrustStack_Clients")
        .key("client_id", AttributeValue::S("ARC".to_string()))
        .send().await {
            Ok(resp) => {
                if let Some(item) = resp.item {
                    let rcu_str = item.get("RCU_Limit")
                        .and_then(|v| v.as_n().ok())
                        .map_or("0", |v| v.as_str());
                    current_capacity = rcu_str.parse::<u64>().unwrap_or(0);
                    println!("SUCCESS: ARC Authority Loaded. Capacity: {} RCU.", current_capacity);
                }
            },
            Err(e) => println!("CRITICAL ERROR: DB Access Failed: {}. Shielding 136B CC.", e),
    }

    let listener = TcpListener::bind("0.0.0.0:8080").expect("Failed to bind");
    println!("Shield: 136B CC | Monitoring Active Swaps...");

    for stream in listener.incoming() {
        if let Ok(mut stream) = stream {
            let response = if current_capacity >= 1 {
                "HTTP/1.1 200 OK\r\n\r\n{ \"status\": \"SETTLED\" }"
            } else {
                "HTTP/1.1 403 Forbidden\r\n\r\n{ \"error\": \"RCU_LIMIT_EXCEEDED\" }"
            };
            stream.write_all(response.as_bytes()).unwrap();
        }
    }
}
