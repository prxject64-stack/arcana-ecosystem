package main

import (
	"fmt"
	"os"
	"strings"
	"github.com/ethereum/go-ethereum/accounts/keystore"
	"github.com/ethereum/go-ethereum/crypto"
)

func main() {
	keyfile := "./data/keystore/UTC--2026-03-02T22-21-49.774515226Z--14a3256052c02f9d87fe1cc3b712d4530061b25c" 
	
	passBytes, err := os.ReadFile("password.txt")
	if err != nil { fmt.Println("Password Error:", err); return }
	password := strings.TrimSpace(string(passBytes))
	
	keyjson, err := os.ReadFile(keyfile)
	if err != nil { fmt.Println("Keyfile Read Error:", err); return }
	
	key, err := keystore.DecryptKey(keyjson, password)
	if err != nil { fmt.Println("Decryption Failed:", err); return }

	privKey := crypto.FromECDSA(key.PrivateKey)
	fmt.Printf("Your KeyHex: %x\n", privKey)
}
