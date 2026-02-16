var bin = "0x6080604052348015600e575f5ffd5b50604051610475380380610475833981016040819052602b91604e565b5f80546001600160a01b0319166001600160a01b03929092169190911790556079565b5f60208284031215605d575f5ffd5b81516001600160a01b03811681146072575f5ffd5b9392505050565b6103ef806100865f395ff3fe608060405234801561000f575f5ffd5b5060043610610060575f3560e01c80633f788a88146100645780635c7995b41461006e578063bd7b09e41461009d578063f3caad03146100b4578063f873575d146100e6578063fccc2813146100f6575b5f5ffd5b61006c6100fd565b005b5f54610080906001600160a01b031681565b6040516001600160a01b0390911681526020015b60405180910390f35b6100a660025481565b604051908152602001610094565b6100d66100c2366004610332565b60016020525f908152604090205460ff1681565b6040519015158152602001610094565b6100a668056bc75e2d6310000081565b6100805f81565b335f9081526001602052604090205460ff16156101615760405162461bcd60e51b815260206004820152601b60248201527f416c7265616479206120436974697a656e206f6620417263616e61000000000060448201526064015b60405180910390fd5b5f546040516370a0823160e01b815233600482015268056bc75e2d63100000916001600160a01b0316906370a0823190602401602060405180830381865afa1580156101af573d5f5f3e3d5ffd5b505050506040513d601f19601f820116820180604052508101906101d3919061035f565b10156102135760405162461bcd60e51b815260206004820152600f60248201526e496e73756666696369656e7420434360881b6044820152606401610158565b5f80546040516323b872dd60e01b8152336004820152602481019290925268056bc75e2d6310000060448301526001600160a01b0316906323b872dd906064016020604051808303815f875af115801561026f573d5f5f3e3d5ffd5b505050506040513d601f19601f820116820180604052508101906102939190610376565b6102cd5760405162461bcd60e51b815260206004820152600b60248201526a109d5c9b8811985a5b195960aa1b6044820152606401610158565b335f9081526001602081905260408220805460ff1916909117905560028054916102f683610395565b909155505060405142815233907f04199342ce6872656761cd4ecbf0c7d377dc6114e642bc738a19c568ce0572a39060200160405180910390a2565b5f60208284031215610342575f5ffd5b81356001600160a01b0381168114610358575f5ffd5b9392505050565b5f6020828403121561036f575f5ffd5b5051919050565b5f60208284031215610386575f5ffd5b81518015158114610358575f5ffd5b5f600182016103b257634e487b7160e01b5f52601160045260245ffd5b506001019056fea26469706673582212206adc670b74d652e4f27571b28356d0c4ccb9247ce066ceb5f40e0f88a6a84a9964736f6c634300081e0033";
var abi = [{"inputs":[{"internalType":"address","name":"_ccTokenAddress","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"citizen","type":"address"},{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"Naturalized","type":"event"},{"inputs":[],"name":"BURN_ADDRESS","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"SACRIFICE_AMOUNT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"ccToken","outputs":[{"internalType":"contract ICCPrivate","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"isCitizen","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"performSacrifice","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"totalCitizens","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}];

console.log("CRITICAL DEPLOYMENT START...");
console.log("Full Payload Size: " + bin.length + " characters");

if (bin.length < 500) {
    console.log("ERROR: Binary data is truncated. Check your .bin file.");
} else {
    var txHash = eth.sendTransaction({
        from: eth.accounts[0],
        data: bin,
        gas: 8000000,
        gasPrice: eth.gasPrice
    });

    console.log("TX Hash: " + txHash);

    while (true) {
        var receipt = eth.getTransactionReceipt(txHash);
        if (receipt && receipt.contractAddress) {
            var code = eth.getCode(receipt.contractAddress);
            console.log("\n--- MASTER LEDGER UPDATE ---");
            console.log("Passport Root: " + receipt.contractAddress);
            console.log("Logic Size:    " + code.length + " bytes");
            
            if (code.length > 2) {
                console.log("STATUS: SUCCESS. Arcana Sovereign is live.");
            } else {
                console.log("STATUS: ERROR. Logic size 2. Constructor reverted.");
            }
            break;
        }
        admin.sleep(1);
    }
}
