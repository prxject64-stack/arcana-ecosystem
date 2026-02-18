const { ethers } = require("ethers");

async function main() {
    const provider = new ethers.JsonRpcProvider("http://127.0.0.1:8545");
    const CC_ADDR = "0xe7f1725e7734ce288f8367e1bb143e90bb3f0512";
    const treasury = new ethers.Wallet("0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80", provider);

    const CC = new ethers.Contract(CC_ADDR, [
        "function transfer(address to, uint256 amount) public returns (bool)",
        "function balanceOf(address) view returns (uint256)"
    ], treasury);

    console.log("--- INITIATING 4,500 PEER SWAP STRESS TEST ---");
    const amount = ethers.parseUnits("1000", 18);
    const swaps = [];

    for (let i = 0; i < 4500; i++) {
        const peer = ethers.Wallet.createRandom().address;
        swaps.push(CC.transfer(peer, amount, { gasLimit: 100000 }));
    }

    const start = Date.now();
    await Promise.all(swaps);
    const end = Date.now();

    console.log(`[+] 4,500 swaps finalized in ${(end - start) / 1000}s`);
}
main().catch(console.error);
