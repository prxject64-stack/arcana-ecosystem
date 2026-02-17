const { ethers } = require("ethers");
const solc = require("solc");
const fs = require("fs");
const path = require("path");

const PORTS = [8549, 8545];
const KEYSTORE_DIR = "data/keystore";
const PASSWORD = "Deezydeezydeezy1$";

const source = '// SPDX-License-Identifier: MIT\npragma solidity ^0.8.20;\ncontract CreditCoinPrivate {\n    string public name = "Credit Coin Private";\n    string public symbol = "CC";\n    uint8 public decimals = 18;\n    uint256 public totalSupply;\n    mapping(address => uint256) public balanceOf;\n    mapping(address => mapping(address => uint256)) public allowance;\n    event Transfer(address indexed from, address indexed to, uint256 value);\n    event Approval(address indexed owner, address indexed spender, uint256 value);\n    constructor() {\n        totalSupply = 136000000000 * 10**18;\n        balanceOf[msg.sender] = totalSupply;\n        emit Transfer(address(0), msg.sender, totalSupply);\n    }\n    function transfer(address to, uint256 value) public returns (bool) {\n        require(balanceOf[msg.sender] >= value, "Insufficient balance");\n        balanceOf[msg.sender] -= value;\n        balanceOf[to] += value;\n        emit Transfer(msg.sender, to, value);\n        return true;\n    }\n}';

async function main() {
    let provider;
    for (let i = 0; i < PORTS.length; i++) {
        const url = "http://127.0.0.1:" + PORTS[i];
        try {
            const p = new ethers.JsonRpcProvider(url);
            await p.getBlockNumber();
            console.log("✅ Connected to Port: " + PORTS[i]);
            provider = p;
            break;
        } catch (e) {}
    }
    if (!provider) throw new Error("❌ No node found on 8549 or 8545.");

    console.log("🔨 Compiling...");
    const input = {
        language: "Solidity",
        sources: { "CC.sol": { content: source } },
        settings: { outputSelection: { "*": { "*": ["*"] } } }
    };
    const output = JSON.parse(solc.compile(JSON.stringify(input)));
    const contractData = output.contracts["CC.sol"]["CreditCoinPrivate"];
    const abi = contractData.abi;
    const bytecode = contractData.evm.bytecode.object;

    const files = fs.readdirSync(KEYSTORE_DIR);
    const keystoreFile = files.find(f => f.startsWith("UTC"));
    const json = fs.readFileSync(path.join(KEYSTORE_DIR, keystoreFile), "utf8");
    const wallet = await ethers.Wallet.fromEncryptedJson(json, PASSWORD);
    const signer = wallet.connect(provider);

    console.log("🚀 Deploying from: " + signer.address);
    const factory = new ethers.ContractFactory(abi, bytecode, signer);
    const contract = await factory.deploy();
    await contract.waitForDeployment();
    
    console.log("---------------------------------------");
    console.log("✅ CC ADDRESS: " + (await contract.getAddress()));
    console.log("---------------------------------------");
}

main().catch(console.error);
