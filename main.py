from web3 import Web3
import json

# Connect to Ethereum network (using Infura)
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Wallet details
sender_address = "0xYourSenderAddress"
private_key = "YourPrivateKey"
receiver_address = "0xReceiverAddress"

# ERC-20 token contract details
token_contract_address = "0xTokenContractAddress"  # Replace with the actual token contract address
token_decimals = 18  # Most ERC-20 tokens use 18 decimals (adjust if needed)

# ABI (Minimal ERC-20 ABI for balance and transfer functions)
erc20_abi = [
    {
        "constant": False,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function"
    }
]

# Load contract
token_contract = web3.eth.contract(address=token_contract_address, abi=erc20_abi)

# Amount of tokens to send (example: sending 10 tokens)
amount = 10
amount_in_wei = int(amount * (10 ** token_decimals))  # Convert to smallest unit

# Get nonce (transaction count for the sender)
nonce = web3.eth.get_transaction_count(sender_address)

# Build transaction
tx = token_contract.functions.transfer(receiver_address, amount_in_wei).build_transaction({
    "chainId": 1,  # Ethereum Mainnet (use 5 for Goerli, 11155111 for Sepolia)
    "gas": 100000,  # Gas limit (adjust based on network conditions)
    "gasPrice": web3.eth.gas_price,
    "nonce": nonce
})

# Sign the transaction
signed_tx = web3.eth.account.sign_transaction(tx, private_key)

# Send the transaction
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

# Print transaction hash
print(f"Transaction sent! Hash: {web3.to_hex(tx_hash)}")
