
const { ethers } = require("ethers");



const partialKey = "0xfdfcd399e13c4f7e1612fd5e655159f899a4951ecf21d153a6adef68474271d";

const targetAddress = "0x14a3256052c02f9d87fe1cc3b712d4530061b25c"; 



const hexChars = "0123456789abcdef";

console.log("Searching for the missing 64th character...");



for (let char of hexChars) {

    const fullKey = partialKey + char;

    try {

        const wallet = new ethers.Wallet(fullKey);

        if (wallet.address.toLowerCase() === targetAddress.toLowerCase()) {

            console.log("\n--------------------------------------------------");

            console.log("MATCH FOUND!");

            console.log("Full Private Key:", fullKey);

            console.log("--------------------------------------------------");

            process.exit(0);

        }

    } catch (e) {}

}

console.log("No match found. Please verify the targetAddress is correct.");

