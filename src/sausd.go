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

// SaunaUSDMetaData contains all meta data concerning the SaunaUSD contract.
var SaunaUSDMetaData = &bind.MetaData{
	ABI: "[{\"inputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"owner\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"spender\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"value\",\"type\":\"uint256\"}],\"name\":\"Approval\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"from\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"to\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"value\",\"type\":\"uint256\"}],\"name\":\"Transfer\",\"type\":\"event\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_minter\",\"type\":\"address\"}],\"name\":\"addMinter\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"name\":\"allowance\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"name\":\"balanceOf\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"decimals\",\"outputs\":[{\"internalType\":\"uint8\",\"name\":\"\",\"type\":\"uint8\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_to\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_value\",\"type\":\"uint256\"}],\"name\":\"mint\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"name\":\"minters\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"name\",\"outputs\":[{\"internalType\":\"string\",\"name\":\"\",\"type\":\"string\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"owner\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"symbol\",\"outputs\":[{\"internalType\":\"string\",\"name\":\"\",\"type\":\"string\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"totalSupply\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_to\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_value\",\"type\":\"uint256\"}],\"name\":\"transfer\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"success\",\"type\":\"bool\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"}]",
}

// SaunaUSDABI is the input ABI used to generate the binding from.
// Deprecated: Use SaunaUSDMetaData.ABI instead.
var SaunaUSDABI = SaunaUSDMetaData.ABI

// SaunaUSD is an auto generated Go binding around an Ethereum contract.
type SaunaUSD struct {
	SaunaUSDCaller     // Read-only binding to the contract
	SaunaUSDTransactor // Write-only binding to the contract
	SaunaUSDFilterer   // Log filterer for contract events
}

// SaunaUSDCaller is an auto generated read-only Go binding around an Ethereum contract.
type SaunaUSDCaller struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// SaunaUSDTransactor is an auto generated write-only Go binding around an Ethereum contract.
type SaunaUSDTransactor struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// SaunaUSDFilterer is an auto generated log filtering Go binding around an Ethereum contract events.
type SaunaUSDFilterer struct {
	contract *bind.BoundContract // Generic contract wrapper for the low level calls
}

// SaunaUSDSession is an auto generated Go binding around an Ethereum contract,
// with pre-set call and transact options.
type SaunaUSDSession struct {
	Contract     *SaunaUSD         // Generic contract binding to set the session for
	CallOpts     bind.CallOpts     // Call options to use throughout this session
	TransactOpts bind.TransactOpts // Transaction auth options to use throughout this session
}

// SaunaUSDCallerSession is an auto generated read-only Go binding around an Ethereum contract,
// with pre-set call options.
type SaunaUSDCallerSession struct {
	Contract *SaunaUSDCaller // Generic contract caller binding to set the session for
	CallOpts bind.CallOpts   // Call options to use throughout this session
}

// SaunaUSDTransactorSession is an auto generated write-only Go binding around an Ethereum contract,
// with pre-set transact options.
type SaunaUSDTransactorSession struct {
	Contract     *SaunaUSDTransactor // Generic contract transactor binding to set the session for
	TransactOpts bind.TransactOpts   // Transaction auth options to use throughout this session
}

// SaunaUSDRaw is an auto generated low-level Go binding around an Ethereum contract.
type SaunaUSDRaw struct {
	Contract *SaunaUSD // Generic contract binding to access the raw methods on
}

// SaunaUSDCallerRaw is an auto generated low-level read-only Go binding around an Ethereum contract.
type SaunaUSDCallerRaw struct {
	Contract *SaunaUSDCaller // Generic read-only contract binding to access the raw methods on
}

// SaunaUSDTransactorRaw is an auto generated low-level write-only Go binding around an Ethereum contract.
type SaunaUSDTransactorRaw struct {
	Contract *SaunaUSDTransactor // Generic write-only contract binding to access the raw methods on
}

// NewSaunaUSD creates a new instance of SaunaUSD, bound to a specific deployed contract.
func NewSaunaUSD(address common.Address, backend bind.ContractBackend) (*SaunaUSD, error) {
	contract, err := bindSaunaUSD(address, backend, backend, backend)
	if err != nil {
		return nil, err
	}
	return &SaunaUSD{SaunaUSDCaller: SaunaUSDCaller{contract: contract}, SaunaUSDTransactor: SaunaUSDTransactor{contract: contract}, SaunaUSDFilterer: SaunaUSDFilterer{contract: contract}}, nil
}

// NewSaunaUSDCaller creates a new read-only instance of SaunaUSD, bound to a specific deployed contract.
func NewSaunaUSDCaller(address common.Address, caller bind.ContractCaller) (*SaunaUSDCaller, error) {
	contract, err := bindSaunaUSD(address, caller, nil, nil)
	if err != nil {
		return nil, err
	}
	return &SaunaUSDCaller{contract: contract}, nil
}

// NewSaunaUSDTransactor creates a new write-only instance of SaunaUSD, bound to a specific deployed contract.
func NewSaunaUSDTransactor(address common.Address, transactor bind.ContractTransactor) (*SaunaUSDTransactor, error) {
	contract, err := bindSaunaUSD(address, nil, transactor, nil)
	if err != nil {
		return nil, err
	}
	return &SaunaUSDTransactor{contract: contract}, nil
}

// NewSaunaUSDFilterer creates a new log filterer instance of SaunaUSD, bound to a specific deployed contract.
func NewSaunaUSDFilterer(address common.Address, filterer bind.ContractFilterer) (*SaunaUSDFilterer, error) {
	contract, err := bindSaunaUSD(address, nil, nil, filterer)
	if err != nil {
		return nil, err
	}
	return &SaunaUSDFilterer{contract: contract}, nil
}

// bindSaunaUSD binds a generic wrapper to an already deployed contract.
func bindSaunaUSD(address common.Address, caller bind.ContractCaller, transactor bind.ContractTransactor, filterer bind.ContractFilterer) (*bind.BoundContract, error) {
	parsed, err := SaunaUSDMetaData.GetAbi()
	if err != nil {
		return nil, err
	}
	return bind.NewBoundContract(address, *parsed, caller, transactor, filterer), nil
}

// Call invokes the (constant) contract method with params as input values and
// sets the output to result. The result type might be a single field for simple
// returns, a slice of interfaces for anonymous returns and a struct for named
// returns.
func (_SaunaUSD *SaunaUSDRaw) Call(opts *bind.CallOpts, result *[]interface{}, method string, params ...interface{}) error {
	return _SaunaUSD.Contract.SaunaUSDCaller.contract.Call(opts, result, method, params...)
}

// Transfer initiates a plain transaction to move funds to the contract, calling
// its default method if one is available.
func (_SaunaUSD *SaunaUSDRaw) Transfer(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _SaunaUSD.Contract.SaunaUSDTransactor.contract.Transfer(opts)
}

// Transact invokes the (paid) contract method with params as input values.
func (_SaunaUSD *SaunaUSDRaw) Transact(opts *bind.TransactOpts, method string, params ...interface{}) (*types.Transaction, error) {
	return _SaunaUSD.Contract.SaunaUSDTransactor.contract.Transact(opts, method, params...)
}

// Call invokes the (constant) contract method with params as input values and
// sets the output to result. The result type might be a single field for simple
// returns, a slice of interfaces for anonymous returns and a struct for named
// returns.
func (_SaunaUSD *SaunaUSDCallerRaw) Call(opts *bind.CallOpts, result *[]interface{}, method string, params ...interface{}) error {
	return _SaunaUSD.Contract.contract.Call(opts, result, method, params...)
}

// Transfer initiates a plain transaction to move funds to the contract, calling
// its default method if one is available.
func (_SaunaUSD *SaunaUSDTransactorRaw) Transfer(opts *bind.TransactOpts) (*types.Transaction, error) {
	return _SaunaUSD.Contract.contract.Transfer(opts)
}

// Transact invokes the (paid) contract method with params as input values.
func (_SaunaUSD *SaunaUSDTransactorRaw) Transact(opts *bind.TransactOpts, method string, params ...interface{}) (*types.Transaction, error) {
	return _SaunaUSD.Contract.contract.Transact(opts, method, params...)
}

// Allowance is a free data retrieval call binding the contract method 0xdd62ed3e.
//
// Solidity: function allowance(address , address ) view returns(uint256)
func (_SaunaUSD *SaunaUSDCaller) Allowance(opts *bind.CallOpts, arg0 common.Address, arg1 common.Address) (*big.Int, error) {
	var out []interface{}
	err := _SaunaUSD.contract.Call(opts, &out, "allowance", arg0, arg1)

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// Allowance is a free data retrieval call binding the contract method 0xdd62ed3e.
//
// Solidity: function allowance(address , address ) view returns(uint256)
func (_SaunaUSD *SaunaUSDSession) Allowance(arg0 common.Address, arg1 common.Address) (*big.Int, error) {
	return _SaunaUSD.Contract.Allowance(&_SaunaUSD.CallOpts, arg0, arg1)
}

// Allowance is a free data retrieval call binding the contract method 0xdd62ed3e.
//
// Solidity: function allowance(address , address ) view returns(uint256)
func (_SaunaUSD *SaunaUSDCallerSession) Allowance(arg0 common.Address, arg1 common.Address) (*big.Int, error) {
	return _SaunaUSD.Contract.Allowance(&_SaunaUSD.CallOpts, arg0, arg1)
}

// BalanceOf is a free data retrieval call binding the contract method 0x70a08231.
//
// Solidity: function balanceOf(address ) view returns(uint256)
func (_SaunaUSD *SaunaUSDCaller) BalanceOf(opts *bind.CallOpts, arg0 common.Address) (*big.Int, error) {
	var out []interface{}
	err := _SaunaUSD.contract.Call(opts, &out, "balanceOf", arg0)

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// BalanceOf is a free data retrieval call binding the contract method 0x70a08231.
//
// Solidity: function balanceOf(address ) view returns(uint256)
func (_SaunaUSD *SaunaUSDSession) BalanceOf(arg0 common.Address) (*big.Int, error) {
	return _SaunaUSD.Contract.BalanceOf(&_SaunaUSD.CallOpts, arg0)
}

// BalanceOf is a free data retrieval call binding the contract method 0x70a08231.
//
// Solidity: function balanceOf(address ) view returns(uint256)
func (_SaunaUSD *SaunaUSDCallerSession) BalanceOf(arg0 common.Address) (*big.Int, error) {
	return _SaunaUSD.Contract.BalanceOf(&_SaunaUSD.CallOpts, arg0)
}

// Decimals is a free data retrieval call binding the contract method 0x313ce567.
//
// Solidity: function decimals() view returns(uint8)
func (_SaunaUSD *SaunaUSDCaller) Decimals(opts *bind.CallOpts) (uint8, error) {
	var out []interface{}
	err := _SaunaUSD.contract.Call(opts, &out, "decimals")

	if err != nil {
		return *new(uint8), err
	}

	out0 := *abi.ConvertType(out[0], new(uint8)).(*uint8)

	return out0, err

}

// Decimals is a free data retrieval call binding the contract method 0x313ce567.
//
// Solidity: function decimals() view returns(uint8)
func (_SaunaUSD *SaunaUSDSession) Decimals() (uint8, error) {
	return _SaunaUSD.Contract.Decimals(&_SaunaUSD.CallOpts)
}

// Decimals is a free data retrieval call binding the contract method 0x313ce567.
//
// Solidity: function decimals() view returns(uint8)
func (_SaunaUSD *SaunaUSDCallerSession) Decimals() (uint8, error) {
	return _SaunaUSD.Contract.Decimals(&_SaunaUSD.CallOpts)
}

// Minters is a free data retrieval call binding the contract method 0xf46eccc4.
//
// Solidity: function minters(address ) view returns(bool)
func (_SaunaUSD *SaunaUSDCaller) Minters(opts *bind.CallOpts, arg0 common.Address) (bool, error) {
	var out []interface{}
	err := _SaunaUSD.contract.Call(opts, &out, "minters", arg0)

	if err != nil {
		return *new(bool), err
	}

	out0 := *abi.ConvertType(out[0], new(bool)).(*bool)

	return out0, err

}

// Minters is a free data retrieval call binding the contract method 0xf46eccc4.
//
// Solidity: function minters(address ) view returns(bool)
func (_SaunaUSD *SaunaUSDSession) Minters(arg0 common.Address) (bool, error) {
	return _SaunaUSD.Contract.Minters(&_SaunaUSD.CallOpts, arg0)
}

// Minters is a free data retrieval call binding the contract method 0xf46eccc4.
//
// Solidity: function minters(address ) view returns(bool)
func (_SaunaUSD *SaunaUSDCallerSession) Minters(arg0 common.Address) (bool, error) {
	return _SaunaUSD.Contract.Minters(&_SaunaUSD.CallOpts, arg0)
}

// Name is a free data retrieval call binding the contract method 0x06fdde03.
//
// Solidity: function name() view returns(string)
func (_SaunaUSD *SaunaUSDCaller) Name(opts *bind.CallOpts) (string, error) {
	var out []interface{}
	err := _SaunaUSD.contract.Call(opts, &out, "name")

	if err != nil {
		return *new(string), err
	}

	out0 := *abi.ConvertType(out[0], new(string)).(*string)

	return out0, err

}

// Name is a free data retrieval call binding the contract method 0x06fdde03.
//
// Solidity: function name() view returns(string)
func (_SaunaUSD *SaunaUSDSession) Name() (string, error) {
	return _SaunaUSD.Contract.Name(&_SaunaUSD.CallOpts)
}

// Name is a free data retrieval call binding the contract method 0x06fdde03.
//
// Solidity: function name() view returns(string)
func (_SaunaUSD *SaunaUSDCallerSession) Name() (string, error) {
	return _SaunaUSD.Contract.Name(&_SaunaUSD.CallOpts)
}

// Owner is a free data retrieval call binding the contract method 0x8da5cb5b.
//
// Solidity: function owner() view returns(address)
func (_SaunaUSD *SaunaUSDCaller) Owner(opts *bind.CallOpts) (common.Address, error) {
	var out []interface{}
	err := _SaunaUSD.contract.Call(opts, &out, "owner")

	if err != nil {
		return *new(common.Address), err
	}

	out0 := *abi.ConvertType(out[0], new(common.Address)).(*common.Address)

	return out0, err

}

// Owner is a free data retrieval call binding the contract method 0x8da5cb5b.
//
// Solidity: function owner() view returns(address)
func (_SaunaUSD *SaunaUSDSession) Owner() (common.Address, error) {
	return _SaunaUSD.Contract.Owner(&_SaunaUSD.CallOpts)
}

// Owner is a free data retrieval call binding the contract method 0x8da5cb5b.
//
// Solidity: function owner() view returns(address)
func (_SaunaUSD *SaunaUSDCallerSession) Owner() (common.Address, error) {
	return _SaunaUSD.Contract.Owner(&_SaunaUSD.CallOpts)
}

// Symbol is a free data retrieval call binding the contract method 0x95d89b41.
//
// Solidity: function symbol() view returns(string)
func (_SaunaUSD *SaunaUSDCaller) Symbol(opts *bind.CallOpts) (string, error) {
	var out []interface{}
	err := _SaunaUSD.contract.Call(opts, &out, "symbol")

	if err != nil {
		return *new(string), err
	}

	out0 := *abi.ConvertType(out[0], new(string)).(*string)

	return out0, err

}

// Symbol is a free data retrieval call binding the contract method 0x95d89b41.
//
// Solidity: function symbol() view returns(string)
func (_SaunaUSD *SaunaUSDSession) Symbol() (string, error) {
	return _SaunaUSD.Contract.Symbol(&_SaunaUSD.CallOpts)
}

// Symbol is a free data retrieval call binding the contract method 0x95d89b41.
//
// Solidity: function symbol() view returns(string)
func (_SaunaUSD *SaunaUSDCallerSession) Symbol() (string, error) {
	return _SaunaUSD.Contract.Symbol(&_SaunaUSD.CallOpts)
}

// TotalSupply is a free data retrieval call binding the contract method 0x18160ddd.
//
// Solidity: function totalSupply() view returns(uint256)
func (_SaunaUSD *SaunaUSDCaller) TotalSupply(opts *bind.CallOpts) (*big.Int, error) {
	var out []interface{}
	err := _SaunaUSD.contract.Call(opts, &out, "totalSupply")

	if err != nil {
		return *new(*big.Int), err
	}

	out0 := *abi.ConvertType(out[0], new(*big.Int)).(**big.Int)

	return out0, err

}

// TotalSupply is a free data retrieval call binding the contract method 0x18160ddd.
//
// Solidity: function totalSupply() view returns(uint256)
func (_SaunaUSD *SaunaUSDSession) TotalSupply() (*big.Int, error) {
	return _SaunaUSD.Contract.TotalSupply(&_SaunaUSD.CallOpts)
}

// TotalSupply is a free data retrieval call binding the contract method 0x18160ddd.
//
// Solidity: function totalSupply() view returns(uint256)
func (_SaunaUSD *SaunaUSDCallerSession) TotalSupply() (*big.Int, error) {
	return _SaunaUSD.Contract.TotalSupply(&_SaunaUSD.CallOpts)
}

// AddMinter is a paid mutator transaction binding the contract method 0x983b2d56.
//
// Solidity: function addMinter(address _minter) returns()
func (_SaunaUSD *SaunaUSDTransactor) AddMinter(opts *bind.TransactOpts, _minter common.Address) (*types.Transaction, error) {
	return _SaunaUSD.contract.Transact(opts, "addMinter", _minter)
}

// AddMinter is a paid mutator transaction binding the contract method 0x983b2d56.
//
// Solidity: function addMinter(address _minter) returns()
func (_SaunaUSD *SaunaUSDSession) AddMinter(_minter common.Address) (*types.Transaction, error) {
	return _SaunaUSD.Contract.AddMinter(&_SaunaUSD.TransactOpts, _minter)
}

// AddMinter is a paid mutator transaction binding the contract method 0x983b2d56.
//
// Solidity: function addMinter(address _minter) returns()
func (_SaunaUSD *SaunaUSDTransactorSession) AddMinter(_minter common.Address) (*types.Transaction, error) {
	return _SaunaUSD.Contract.AddMinter(&_SaunaUSD.TransactOpts, _minter)
}

// Mint is a paid mutator transaction binding the contract method 0x40c10f19.
//
// Solidity: function mint(address _to, uint256 _value) returns()
func (_SaunaUSD *SaunaUSDTransactor) Mint(opts *bind.TransactOpts, _to common.Address, _value *big.Int) (*types.Transaction, error) {
	return _SaunaUSD.contract.Transact(opts, "mint", _to, _value)
}

// Mint is a paid mutator transaction binding the contract method 0x40c10f19.
//
// Solidity: function mint(address _to, uint256 _value) returns()
func (_SaunaUSD *SaunaUSDSession) Mint(_to common.Address, _value *big.Int) (*types.Transaction, error) {
	return _SaunaUSD.Contract.Mint(&_SaunaUSD.TransactOpts, _to, _value)
}

// Mint is a paid mutator transaction binding the contract method 0x40c10f19.
//
// Solidity: function mint(address _to, uint256 _value) returns()
func (_SaunaUSD *SaunaUSDTransactorSession) Mint(_to common.Address, _value *big.Int) (*types.Transaction, error) {
	return _SaunaUSD.Contract.Mint(&_SaunaUSD.TransactOpts, _to, _value)
}

// Transfer is a paid mutator transaction binding the contract method 0xa9059cbb.
//
// Solidity: function transfer(address _to, uint256 _value) returns(bool success)
func (_SaunaUSD *SaunaUSDTransactor) Transfer(opts *bind.TransactOpts, _to common.Address, _value *big.Int) (*types.Transaction, error) {
	return _SaunaUSD.contract.Transact(opts, "transfer", _to, _value)
}

// Transfer is a paid mutator transaction binding the contract method 0xa9059cbb.
//
// Solidity: function transfer(address _to, uint256 _value) returns(bool success)
func (_SaunaUSD *SaunaUSDSession) Transfer(_to common.Address, _value *big.Int) (*types.Transaction, error) {
	return _SaunaUSD.Contract.Transfer(&_SaunaUSD.TransactOpts, _to, _value)
}

// Transfer is a paid mutator transaction binding the contract method 0xa9059cbb.
//
// Solidity: function transfer(address _to, uint256 _value) returns(bool success)
func (_SaunaUSD *SaunaUSDTransactorSession) Transfer(_to common.Address, _value *big.Int) (*types.Transaction, error) {
	return _SaunaUSD.Contract.Transfer(&_SaunaUSD.TransactOpts, _to, _value)
}

// SaunaUSDApprovalIterator is returned from FilterApproval and is used to iterate over the raw logs and unpacked data for Approval events raised by the SaunaUSD contract.
type SaunaUSDApprovalIterator struct {
	Event *SaunaUSDApproval // Event containing the contract specifics and raw log

	contract *bind.BoundContract // Generic contract to use for unpacking event data
	event    string              // Event name to use for unpacking event data

	logs chan types.Log        // Log channel receiving the found contract events
	sub  ethereum.Subscription // Subscription for errors, completion and termination
	done bool                  // Whether the subscription completed delivering logs
	fail error                 // Occurred error to stop iteration
}

// Next advances the iterator to the subsequent event, returning whether there
// are any more events found. In case of a retrieval or parsing error, false is
// returned and Error() can be queried for the exact failure.
func (it *SaunaUSDApprovalIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(SaunaUSDApproval)
			if err := it.contract.UnpackLog(it.Event, it.event, log); err != nil {
				it.fail = err
				return false
			}
			it.Event.Raw = log
			return true

		default:
			return false
		}
	}
	// Iterator still in progress, wait for either a data or an error event
	select {
	case log := <-it.logs:
		it.Event = new(SaunaUSDApproval)
		if err := it.contract.UnpackLog(it.Event, it.event, log); err != nil {
			it.fail = err
			return false
		}
		it.Event.Raw = log
		return true

	case err := <-it.sub.Err():
		it.done = true
		it.fail = err
		return it.Next()
	}
}

// Error returns any retrieval or parsing error occurred during filtering.
func (it *SaunaUSDApprovalIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *SaunaUSDApprovalIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// SaunaUSDApproval represents a Approval event raised by the SaunaUSD contract.
type SaunaUSDApproval struct {
	Owner   common.Address
	Spender common.Address
	Value   *big.Int
	Raw     types.Log // Blockchain specific contextual infos
}

// FilterApproval is a free log retrieval operation binding the contract event 0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925.
//
// Solidity: event Approval(address indexed owner, address indexed spender, uint256 value)
func (_SaunaUSD *SaunaUSDFilterer) FilterApproval(opts *bind.FilterOpts, owner []common.Address, spender []common.Address) (*SaunaUSDApprovalIterator, error) {

	var ownerRule []interface{}
	for _, ownerItem := range owner {
		ownerRule = append(ownerRule, ownerItem)
	}
	var spenderRule []interface{}
	for _, spenderItem := range spender {
		spenderRule = append(spenderRule, spenderItem)
	}

	logs, sub, err := _SaunaUSD.contract.FilterLogs(opts, "Approval", ownerRule, spenderRule)
	if err != nil {
		return nil, err
	}
	return &SaunaUSDApprovalIterator{contract: _SaunaUSD.contract, event: "Approval", logs: logs, sub: sub}, nil
}

// WatchApproval is a free log subscription operation binding the contract event 0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925.
//
// Solidity: event Approval(address indexed owner, address indexed spender, uint256 value)
func (_SaunaUSD *SaunaUSDFilterer) WatchApproval(opts *bind.WatchOpts, sink chan<- *SaunaUSDApproval, owner []common.Address, spender []common.Address) (event.Subscription, error) {

	var ownerRule []interface{}
	for _, ownerItem := range owner {
		ownerRule = append(ownerRule, ownerItem)
	}
	var spenderRule []interface{}
	for _, spenderItem := range spender {
		spenderRule = append(spenderRule, spenderItem)
	}

	logs, sub, err := _SaunaUSD.contract.WatchLogs(opts, "Approval", ownerRule, spenderRule)
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(SaunaUSDApproval)
				if err := _SaunaUSD.contract.UnpackLog(event, "Approval", log); err != nil {
					return err
				}
				event.Raw = log

				select {
				case sink <- event:
				case err := <-sub.Err():
					return err
				case <-quit:
					return nil
				}
			case err := <-sub.Err():
				return err
			case <-quit:
				return nil
			}
		}
	}), nil
}

// ParseApproval is a log parse operation binding the contract event 0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925.
//
// Solidity: event Approval(address indexed owner, address indexed spender, uint256 value)
func (_SaunaUSD *SaunaUSDFilterer) ParseApproval(log types.Log) (*SaunaUSDApproval, error) {
	event := new(SaunaUSDApproval)
	if err := _SaunaUSD.contract.UnpackLog(event, "Approval", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}

// SaunaUSDTransferIterator is returned from FilterTransfer and is used to iterate over the raw logs and unpacked data for Transfer events raised by the SaunaUSD contract.
type SaunaUSDTransferIterator struct {
	Event *SaunaUSDTransfer // Event containing the contract specifics and raw log

	contract *bind.BoundContract // Generic contract to use for unpacking event data
	event    string              // Event name to use for unpacking event data

	logs chan types.Log        // Log channel receiving the found contract events
	sub  ethereum.Subscription // Subscription for errors, completion and termination
	done bool                  // Whether the subscription completed delivering logs
	fail error                 // Occurred error to stop iteration
}

// Next advances the iterator to the subsequent event, returning whether there
// are any more events found. In case of a retrieval or parsing error, false is
// returned and Error() can be queried for the exact failure.
func (it *SaunaUSDTransferIterator) Next() bool {
	// If the iterator failed, stop iterating
	if it.fail != nil {
		return false
	}
	// If the iterator completed, deliver directly whatever's available
	if it.done {
		select {
		case log := <-it.logs:
			it.Event = new(SaunaUSDTransfer)
			if err := it.contract.UnpackLog(it.Event, it.event, log); err != nil {
				it.fail = err
				return false
			}
			it.Event.Raw = log
			return true

		default:
			return false
		}
	}
	// Iterator still in progress, wait for either a data or an error event
	select {
	case log := <-it.logs:
		it.Event = new(SaunaUSDTransfer)
		if err := it.contract.UnpackLog(it.Event, it.event, log); err != nil {
			it.fail = err
			return false
		}
		it.Event.Raw = log
		return true

	case err := <-it.sub.Err():
		it.done = true
		it.fail = err
		return it.Next()
	}
}

// Error returns any retrieval or parsing error occurred during filtering.
func (it *SaunaUSDTransferIterator) Error() error {
	return it.fail
}

// Close terminates the iteration process, releasing any pending underlying
// resources.
func (it *SaunaUSDTransferIterator) Close() error {
	it.sub.Unsubscribe()
	return nil
}

// SaunaUSDTransfer represents a Transfer event raised by the SaunaUSD contract.
type SaunaUSDTransfer struct {
	From  common.Address
	To    common.Address
	Value *big.Int
	Raw   types.Log // Blockchain specific contextual infos
}

// FilterTransfer is a free log retrieval operation binding the contract event 0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef.
//
// Solidity: event Transfer(address indexed from, address indexed to, uint256 value)
func (_SaunaUSD *SaunaUSDFilterer) FilterTransfer(opts *bind.FilterOpts, from []common.Address, to []common.Address) (*SaunaUSDTransferIterator, error) {

	var fromRule []interface{}
	for _, fromItem := range from {
		fromRule = append(fromRule, fromItem)
	}
	var toRule []interface{}
	for _, toItem := range to {
		toRule = append(toRule, toItem)
	}

	logs, sub, err := _SaunaUSD.contract.FilterLogs(opts, "Transfer", fromRule, toRule)
	if err != nil {
		return nil, err
	}
	return &SaunaUSDTransferIterator{contract: _SaunaUSD.contract, event: "Transfer", logs: logs, sub: sub}, nil
}

// WatchTransfer is a free log subscription operation binding the contract event 0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef.
//
// Solidity: event Transfer(address indexed from, address indexed to, uint256 value)
func (_SaunaUSD *SaunaUSDFilterer) WatchTransfer(opts *bind.WatchOpts, sink chan<- *SaunaUSDTransfer, from []common.Address, to []common.Address) (event.Subscription, error) {

	var fromRule []interface{}
	for _, fromItem := range from {
		fromRule = append(fromRule, fromItem)
	}
	var toRule []interface{}
	for _, toItem := range to {
		toRule = append(toRule, toItem)
	}

	logs, sub, err := _SaunaUSD.contract.WatchLogs(opts, "Transfer", fromRule, toRule)
	if err != nil {
		return nil, err
	}
	return event.NewSubscription(func(quit <-chan struct{}) error {
		defer sub.Unsubscribe()
		for {
			select {
			case log := <-logs:
				// New log arrived, parse the event and forward to the user
				event := new(SaunaUSDTransfer)
				if err := _SaunaUSD.contract.UnpackLog(event, "Transfer", log); err != nil {
					return err
				}
				event.Raw = log

				select {
				case sink <- event:
				case err := <-sub.Err():
					return err
				case <-quit:
					return nil
				}
			case err := <-sub.Err():
				return err
			case <-quit:
				return nil
			}
		}
	}), nil
}

// ParseTransfer is a log parse operation binding the contract event 0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef.
//
// Solidity: event Transfer(address indexed from, address indexed to, uint256 value)
func (_SaunaUSD *SaunaUSDFilterer) ParseTransfer(log types.Log) (*SaunaUSDTransfer, error) {
	event := new(SaunaUSDTransfer)
	if err := _SaunaUSD.contract.UnpackLog(event, "Transfer", log); err != nil {
		return nil, err
	}
	event.Raw = log
	return event, nil
}
