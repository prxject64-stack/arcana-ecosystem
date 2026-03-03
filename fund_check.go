package main

import (
	"context"
	"fmt"
	"math/big"
	"github.com/ethereum/go-ethereum/common"
	"github.com/ethereum/go-ethereum/ethclient"
	"arcana-ecosystem/contracts" // Points to your generated sausd.go
)

func main() {
	client, _ := ethclient.Dial("./data/geth.ipc")
	sausdAddr := common.HexToAddress("0xC2ED94f54e87D71a0356beAb5fbE8913063A24b2")
	psmAddr := common.HexToAddress("0x5edcff1af1ffd54d64f2f734c0fac8aea1caad6d")
	
	instance, err := contracts.NewSaunaUSD(sausdAddr, client)
	if err != nil { fmt.Println("Binding Error:", err); return }

	bal, err := instance.BalanceOf(nil, psmAddr)
	if err != nil { fmt.Println("Call Error:", err); return }

	fmt.Printf("PSM Balance: %s saUSD\n", bal.String())
}
