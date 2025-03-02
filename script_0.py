
import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Retrieve values from .env
RPC_URL = os.getenv("RPC_URL")

# Connect to the blockchain node
w3 = Web3(Web3.HTTPProvider(RPC_URL))

if w3.is_connected():
    print(" Connected to Legion Crypto")
else:
    print(" Connection failed")

print(f"Performing blockchain info check: w3.eth.get_accounts()")
print(f"Web3 is connected: {w3.is_connected}")
print(f"Commit Number: 0")
print(f"Random number: 7")
