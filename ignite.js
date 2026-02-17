console.log("Attempting Sovereign Ignition...");
var account = "0x8d11448f255863E8E4023549297052C4a11dAf13";
var unlocked = personal.unlockAccount(account, "Deezydeezydeezy1$", 0);
console.log("Account Unlocked: " + unlocked);

if (unlocked) {
  miner.start();
  console.log("Miner started successfully.");
} else {
  console.log("FATAL: Could not unlock account.");
}
