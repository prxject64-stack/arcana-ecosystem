async function runSovereignSauna() {
    console.log("--- r7iz.4xlarge: UNLOCKING & STARTING 4,500 SWAPS ---");
    const sender = eth.coinbase;
    const password = "Deezydeezydeezy1$";
    const receiver = "0xC773179F184BA9a895B5e5C85aa5D1a5Ea3556b0";

    // Unlock the account for 3600 seconds (1 hour) to handle the load
    try {
        personal.unlockAccount(sender, password, 3600);
        console.log("Account Unlocked.");
    } catch (e) {
        console.log("Unlock Failed: " + e);
        return;
    }

    let nextNonce = eth.getTransactionCount(sender, "pending");

    for (let i = 0; i < 4500; i++) {
        try {
            eth.sendTransaction({
                from: sender,
                to: receiver,
                value: web3.toWei(0.1, "ether"),
                gasPrice: "1000000000",
                nonce: nextNonce
            });
            nextNonce++;
            if (i % 500 === 0) console.log("Broadcasting swap #" + i + "...");
        } catch (e) {
            console.log("Error at index " + i + ": " + e);
            break;
        }
    }
    console.log("--- BROADCAST COMPLETE: 4,500 SWAPS QUEUED ---");
}
runSovereignSauna();
