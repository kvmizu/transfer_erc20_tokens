# ERC-20 Token Transfer Script

This script allows you to transfer **ERC-20 tokens** from one wallet to another on the Ethereum blockchain using **Web3.py**.

## Prerequisites

### Install Dependencies
Make sure you have Python installed and install the required package:
```sh
pip install web3
```

### Get an Ethereum Node Provider
You need access to an Ethereum node provider such as **Infura** or **Alchemy**:
- Sign up at [Infura](https://infura.io/) and create a new project.
- Get your **Infura Project ID**.

### Gather Required Details
- **Your Ethereum Wallet Address** (Sender)
- **Your Private Key** (Do **not** share this publicly)
- **Recipient Address**
- **ERC-20 Token Contract Address**
- **Token Decimals** (Most ERC-20 tokens use 18 decimals, check the token’s details)

## Configuration
Before running the script, update the following variables in `erc20_transfer.py`:
```python
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
sender_address = "0xYourSenderAddress"
private_key = "YourPrivateKey"
receiver_address = "0xReceiverAddress"
token_contract_address = "0xTokenContractAddress"
token_decimals = 18  # Adjust if needed
amount = 10  # Number of tokens to send
```

## Running the Script
Run the script with:
```sh
python erc20_transfer.py
```
If the transaction is successful, you will see an output like:
```sh
Transaction sent! Hash: 0x123456789...
```

## Notes
- **Ensure you have enough ETH in your wallet** to cover gas fees.
- This script works for **any ERC-20 token**; just update the contract address.
- **Test on Goerli or Sepolia testnets** before using real tokens.
- **Never expose your private key** in public or shared environments.

## License
This project is licensed under the MIT License.

## Disclaimer
Use this script at your own risk. The author is not responsible for any lost funds due to incorrect usage or security breaches.

