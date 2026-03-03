package main

import (
	"context"
	"fmt"
	"math/big"
	"net"
	"time"

	"github.com/ethereum/go-ethereum/common"
	"github.com/ethereum/go-ethereum/core/types"
	"github.com/ethereum/go-ethereum/crypto"
	"github.com/ethereum/go-ethereum/ethclient"
)

func main() {
	// Use ethclient only for setup
	client, _ := ethclient.Dial("./data/geth.ipc")
	privateKey, _ := crypto.HexToECDSA("fdfcd399e13c4f7e1612fd5e655159f899a4951ecf21d153a6adef68474271d2")
	fromAddress := common.HexToAddress("0x14a3256052c02f9d87fe1cc3b712d4530061b25c")
	toAddress := common.HexToAddress("0x179119B999F69006096333604931083916960E01")
	
	nonce, _ := client.PendingNonceAt(context.Background(), fromAddress)
	chainID, _ := client.NetworkID(context.Background())
	gasPrice, _ := client.SuggestGasPrice(context.Background())
	client.Close()

	fmt.Printf("Pre-signing 4500 transactions for 136B CC-P pool...\n")
	payloads := make([][]byte, 4500)
	for i := 0; i < 4500; i++ {
		tx := types.NewTransaction(nonce+uint64(i), toAddress, big.NewInt(100000000000000), 21000, gasPrice, nil)
		signedTx, _ := types.SignTx(tx, types.NewEIP155Signer(chainID), privateKey)
		rawTx, _ := signedTx.MarshalBinary()
		
		// Construct raw JSON-RPC string manually to save CPU
		req := fmt.Sprintf(`{"jsonrpc":"2.0","method":"eth_sendRawTransaction","params":["0x%x"],"id":%d}\n`, rawTx, i)
		payloads[i] = []byte(req)
	}

	// Direct Unix Socket Connection
	conn, _ := net.Dial("unix", "./data/geth.ipc")
	defer conn.Close()

	fmt.Println("Launching Raw Pipe Stream...")
	start := time.Now()
	
	// Stream everything into the pipe in one go
	for _, p := range payloads {
		conn.Write(p)
	}
	
	latency := time.Since(start)
	fmt.Printf("Submission Latency: %v\n", latency)
}
