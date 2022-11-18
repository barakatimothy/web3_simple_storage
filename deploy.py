import imp
import json
from traceback import print_tb
from solcx import compilestandard
from web3 import web3
from dotenv import load_dorenv
with open("./simplestorage.sol", "r") as file:
    Simple_Storage_file=file.read()
## install pysolcx
comipiled_sol  = compilestandard(
    {
        'language':'solidity',
        'sources':{'simplestorage.sol':{"content":Simple_Storage_file}},
        'settings':{'outputselection':
        {
            '*':{"*":["abi ","metadta","evm.bytecode","evm.sourceMap"]}}}},
    solc_version="0.6.0"
)
print(comipiled_sol)

with open("compiled_code.json","w") as file:
    json.dump(comipiled_sol,file)
    ##deploy code get the bytecode
bytecode=comipiled_sol['contracts']['simplestorage.sol']['simplestorage']['evm']['bytecode']['object']
##get ABI   
abi = comipiled_sol['contracts']['simplestorage.sol']['simplestorage']['abi']
print(abi)
##deploy to ganache to create and spin up local blockchain


#connect to ganache
w3= Web3(web3.HTTPProvider("http:0.0.0.0:8545"))
chain_id=1337
my_address='the address'
private_key=os.getenv('PRIVATE_KEY')

#create a contract in python
simplestorage=w3.eth.contract(abi=abi,bytecode=bytecode)
print(simplestorage)

Nonce=w3.eth.getTransactionCount(my_address)
print(Nonce)
#build transaction
print("deploying Contract...")
transaction = simplestorage.constructor().buildTransaction({"chainid":chain_id,"address":my_address,"Nonce":Nonce})
signed_txn =w3.eth.account.sign_transaction(transaction,private_key=private_key)
tx_hash= w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt=w3.eth.wait_for_Transaction_receipt(tx_hash
)



##working inside that contract 1.ABI 2. Address
simplestorage =w3.eth.contract(address = tx_receipt.contractAddress, abi = abi)
#call --> simulate and get return value 
#transact ---> makes state change on blockchain
print('Deployed!')
print(simplestorage.functions.retrieve().call())
print(simplestorage.functions.store(15).call())

print ("updating Contract...")
store_transaction = simplestorage.functions.store(15).buildTransaction({
    "chainId":chain_id,"Nonce":Nonce +1,"from":my_address
})
signed_store_txn=w3.eth.account.sign_transaction(
    store_transaction,private_key=private_key)

send_store_tx =w3.eth.send_raw_Transaction(signed_store_txn.rawTransaction)
tx_receipt =w3.eth.wait_for_transaxtion_receipt( send_store_tx)
print("updated!")
#install nodejs 
#install yarn 
#install ganache-cli  eg. yarn ganache-cli ...