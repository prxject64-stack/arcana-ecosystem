// Code generated - DO NOT EDIT.
// This file is a generated binding and any manual changes will be lost.

package contracts

import (
	"errors"
	"math/big"
	"strings"

	ethereum "github.com/ethereum/go-ethereum"
	"github.com/ethereum/go-ethereum/accounts/abi"
	"github.com/ethereum/go-ethereum/accounts/abi/bind"
	"github.com/ethereum/go-ethereum/common"
	"github.com/ethereum/go-ethereum/core/types"
	"github.com/ethereum/go-ethereum/event"
)

// Reference imports to suppress errors if they are not otherwise used.
var (
	_ = errors.New
	_ = big.NewInt
	_ = strings.NewReader
	_ = ethereum.NotFound
	_ = bind.Bind
	_ = common.Big1
	_ = types.BloomLookup
	_ = event.NewSubscription
	_ = abi.ConvertType
)

// PSMMetaData contains all meta data concerning the PSM contract.
var PSMMetaData = &bind.MetaData{
	ABI: "[{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_ccp\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"_sausd\",\"type\":\"address\"}],\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"},{\"inputs\":[],\"name\":\"admin\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"ccp\",\"outputs\":[{\"internalType\":\"contractIERC20\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"sausd\",\"outputs\":[{\"internalType\":\"contractIERC20\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"}],\"name\":\"swapCCtoSA\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"}]",
}

// PSMABI is the input ABI used to generate the binding from.
// Deprecated: Use PSMMetaData.ABI instead.
var PSMABI = PSMMetaData.ABI

// PSM is an auto generated Go binding around an Ethereum contract.
type PSM struct {
	PSMCaller     // Read-only binding to the contract
	PSMTransactor // Write-only binding to the contract
	PSMFilterer   // Log filterer for contract events
}

// PSMCaller is an auto generated read-only Go binding around an Ethereum contract.
type PSMCaller struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// PSMTransactor is an auto generated write-only Go binding around an Ethereum contract.
type PSMTransactor struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// PSMFilterer is an auto generated log filtering Go binding around an Ethereum contract events.
type PSMFilterer struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// PSMSession is an auto generated Go binding around an Ethereum contract,
// with pre-set call and transact options.
type PSMSession struct {
	Contract     *PSM              // Generic contract binding to set the session for
	CallOpts     bind.CallOpts     // Call options to use throughout this session
	TransactOpts bind.TransactOpts // Transaction auth options to use throughout this session
}

// PSMCallerSession is an auto generated read-only Go binding around an Ethereum contract,
// with pre-set call options.
type PSMCallerSession struct {
	Contract *PSMCaller    // Generic contract caller binding to set the session for
	CallOpts bind.CallOpts // Call options to use throughout this session
}

// PSMTransactorSession is an auto generated write-only Go binding around an Ethereum contract,
// with pre-set transact options.
type PSMTransactorSession struct {
	Contract     *PSMTransactor    // Generic contract transactor binding to set the session for
	TransactOpts bind.TransactOpts // Transaction auth options to use throughout this session
}

// PSMRaw is an auto generated low-level Go binding around an Ethereum contract.
type PSMRaw struct {
	Contract *PSM // Generic contract binding to access the raw methods on
}

// PSMCallerRaw is an auto generated low-level read-only Go binding around an Ethereum contract.
type PSMCallerRaw struct {
	Contract *PSMCaller // Generic read-only contract binding to access the raw methods on
}

// PSMTransactorRaw is an auto generated low-level write-only Go binding around an Ethereum contract.
type PSMTransactorRaw struct {
	Contract *PSMTransactor // Generic write-only contract binding to access the raw methods on
}

// NewPSM creates a new instance of PSM, bound to a specific deployed contract.
func NewPSM(address common.Address, backend bind.ContractBackend) (*PSM, error) {
	contract, err := bindPSM(address, backend, backend, backend)
	if err != nil {
		return nil, err
	}
	return &PSM{PSMCaller: PSMCaller{contract: contract}, PSMTransactor: PSMTransactor{contract: contract}, PSMFilterer: PSMFilterer{contract: contract}}, nil
}

// NewPSMCaller creates a new read-only instance of PSM, bound to a specific deployed contract.
func NewPSMCaller(address common.Address, caller bind.ContractCaller) (*PSMCaller, error) {
	contract, err := bindPSM(address, caller, nil, nil)
	if err != nil {
		return nil, err
	}
	return &PSMCaller{contract: contract}, nil
}

// NewPSMTransactor creates a new write-only instance of PSM, bound to a specific deployed contract.
func NewPSMTransactor(address common.Address, transactor bind.ContractTransactor) (*PSMTransactor, error) {
	contract, err := bindPSM(address, nil, transactor, nil)
	if err != nil {
		return nil, err
	}
	return &PSMTransactor{contract: contract}, nil
}

// NewPSMFilterer creates a new log filterer instance of PSM, bound to a specific deployed contract.
func NewPSMFilterer(address common.Address, filterer bind.ContractFilterer) (*PSMFilterer, error) {
	contract, err := bindPSM(address, nil, nil, filterer)
	if err != nil {
		return nil, err
	}
	return &PSMFilterer{contract: contract}, nil
}

// bindPSM binds a generic wrapper to an already deployed contract.
func bindPSM(address common.Address, caller bind.ContractCaller, transactor bind.ContractTransactor, filterer bind.ContractFilterer) (*bind.BoundContract, error) {
	parsed, err := PSMMetaData.GetAbi()
	if err != nil {
		return nil, err
	}
	return bind.NewBoundContract(address, *parsed, caller, transactor, filterer), nil
}

// Call invokes the (constant) contract method with params as input values and
// sets the output to result. The result type might be a single field for simple
// returns, a slice of interfaces for anonymous returns and a struct for named
// returns.
func (_PSM *PSMRaw) Call(opts *bind.CallOpts, result *[]interface{}, method string, params ...interface{}) error {
	return _PSM.Contract.PSMCaller.contract.Call(opts, result, method, params...)
}

// Transfer initiates a plain transaction to move funds to the contract, calling
// its default method if one is available.
func (_PSM *PSMRaw) Transfer(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _PSM.Contract.PSMTransactor.contract.Transfer(opts)
}

// Transact invokes the (paid) contract method with params as input values.
func (_PSM *PSMRaw) Transact(opts *bind.TransactOpts, method string, params ...interface{}) (*types.Transaction, error) {
	return _PSM.Contract.PSMTransactor.contract.Transact(opts, method, params...)
}

// Call invokes the (constant) contract method with params as input values and
// sets the output to result. The result type might be a single field for simple
// returns, a slice of interfaces for anonymous returns and a struct for named
// returns.
func (_PSM *PSMCallerRaw) Call(opts *bind.CallOpts, result *[]interface{}, method string, params ...interface{}) error {
	return _PSM.Contract.contract.Call(opts, result, method, params...)
}

// Transfer initiates a plain transaction to move funds to the contract, calling
// its default method if one is available.
func (_PSM *PSMTransactorRaw) Transfer(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _PSM.Contract.contract.Transfer(opts)
}

// Transact invokes the (paid) contract method with params as input values.
func (_PSM *PSMTransactorRaw) Transact(opts *bind.TransactOpts, method string, params ...interface{}) (*types.Transaction, error) {
	return _PSM.Contract.contract.Transact(opts, method, params...)
}

// Admin is a free data retrieval call binding the contract method 0xf851a440.
//
// Solidity: function admin() view returns(address)
func (_PSM *PSMCaller) Admin(opts *bind.CallOpts) (common.Address, error) {
	var out []interface{}
	err := _PSM.contract.Call(opts, &out, "admin")

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// Admin is a free data retrieval call binding the contract method 0xf851a440.
//
// Solidity: function admin() view returns(address)
func (_PSM *PSMSession) Admin() (common.Address, error) {
	return _PSM.Contract.Admin(&_PSM.CallOpts)
}

// Admin is a free data retrieval call binding the contract method 0xf851a440.
//
// Solidity: function admin() view returns(address)
func (_PSM *PSMCallerSession) Admin() (common.Address, error) {
	return _PSM.Contract.Admin(&_PSM.CallOpts)
}

// Ccp is a free data retrieval call binding the contract method 0x9cd45e4a.
//
// Solidity: function ccp() view returns(address)
func (_PSM *PSMCaller) Ccp(opts *bind.CallOpts) (common.Address, error) {
	var out []interface{}
	err := _PSM.contract.Call(opts, &out, "ccp")

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// Ccp is a free data retrieval call binding the contract method 0x9cd45e4a.
//
// Solidity: function ccp() view returns(address)
func (_PSM *PSMSession) Ccp() (common.Address, error) {
	return _PSM.Contract.Ccp(&_PSM.CallOpts)
}

// Ccp is a free data retrieval call binding the contract method 0x9cd45e4a.
//
// Solidity: function ccp() view returns(address)
func (_PSM *PSMCallerSession) Ccp() (common.Address, error) {
	return _PSM.Contract.Ccp(&_PSM.CallOpts)
}

// Sausd is a free data retrieval call binding the contract method 0x917d9857.
//
// Solidity: function sausd() view returns(address)
func (_PSM *PSMCaller) Sausd(opts *bind.CallOpts) (common.Address, error) {
	var out []interface{}
	err := _PSM.contract.Call(opts, &out, "sausd")

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// Sausd is a free data retrieval call binding the contract method 0x917d9857.
//
// Solidity: function sausd() view returns(address)
func (_PSM *PSMSession) Sausd() (common.Address, error) {
	return _PSM.Contract.Sausd(&_PSM.CallOpts)
}

// Sausd is a free data retrieval call binding the contract method 0x917d9857.
//
// Solidity: function sausd() view returns(address)
func (_PSM *PSMCallerSession) Sausd() (common.Address, error) {
	return _PSM.Contract.Sausd(&_PSM.CallOpts)
}

// SwapCCtoSA is a paid mutator transaction binding the contract method 0x023aea43.
//
// Solidity: function swapCCtoSA(uint256 amount) returns()
func (_PSM *PSMTransactor) SwapCCtoSA(opts *bind.TransactOpts, amount *big.Int) (*types.Transaction, error) {
	return _PSM.contract.Transact(opts, "swapCCtoSA", amount)
}

// SwapCCtoSA is a paid mutator transaction binding the contract method 0x023aea43.
//
// Solidity: function swapCCtoSA(uint256 amount) returns()
func (_PSM *PSMSession) SwapCCtoSA(amount *big.Int) (*types.Transaction, error) {
	return _PSM.Contract.SwapCCtoSA(&_PSM.TransactOpts, amount)
}

// SwapCCtoSA is a paid mutator transaction binding the contract method 0x023aea43.
//
// Solidity: function swapCCtoSA(uint256 amount) returns()
func (_PSM *PSMTransactorSession) SwapCCtoSA(amount *big.Int) (*types.Transaction, error) {
	return _PSM.Contract.SwapCCtoSA(&_PSM.TransactOpts, amount)
}
