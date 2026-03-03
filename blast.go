package main

import (
	"context"
	"fmt"
	"math/big"
	"sync"
	"arcana-ecosystem/contracts" 
	"github.com/ethereum/go-ethereum/accounts/abi/bind"
	"github.com/ethereum/go-ethereum/common"
	"github.com/ethereum/go-ethereum/crypto"
	"github.com/ethereum/go-ethereum/ethclient"
)

func main() {
	client, err := ethclient.Dial("./data/geth.ipc")
	if err != nil { fmt.Println("Dial Error:", err); return }

	// Master Signer: 0x14a3256052c02f9d87fe1cc3b712d4530061b25c
	keyHex := "fdfcd399e13c4f7e1612fd5e655159f899a4951ecf21d153a6adef68474271d2"
	privateKey, err := crypto.HexToECDSA(keyHex)
	if err != nil { fmt.Println("Key Error (Check Length):", err); return }

	chainID, _ := client.NetworkID(context.Background())
	psmAddr := common.HexToAddress("0x3ca2adc9db908286519aa79a7e5c9b6b72c21644")
	psm, _ := contracts.NewPSM(psmAddr, client)

	fromAddr := common.HexToAddress("0x14a3256052c02f9d87fe1cc3b712d4530061b25c")
	nonce, _ := client.PendingNonceAt(context.Background(), fromAddr)
	amount := big.NewInt(1000000000000000000)

	var wg sync.WaitGroup
	for i := uint64(0); i < 4500; i++ {
		wg.Add(1)
		go func(n uint64) {
			defer wg.Done()
			auth, _ := bind.NewKeyedTransactorWithChainID(privateKey, chainID)
			auth.Nonce = big.NewInt(int64(nonce + n))
			auth.GasLimit = uint64(300000)
			auth.GasPrice, _ = client.SuggestGasPrice(context.Background())

			tx, err := psm.SwapCCtoSA(auth, amount)
			if err != nil {
				fmt.Printf("Tx %d failed: %v\n", n, err)
				return
			}
			fmt.Printf("Tx %d Sent: %s\n", n, tx.Hash().Hex())
		}(i)
	}
	wg.Wait()
	fmt.Println("Blast Injection Complete.")
}
