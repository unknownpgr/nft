import sys
from os import path
sys.path.append(path.abspath('/python-api'))

import base58
import json
from api.metaplex_api import MetaplexAPI
from cryptography.fernet import Fernet

SERVER_DECRYPTION_KEY = Fernet.generate_key().decode("ascii")
PRIVATE_KEY_PATH = '/app/key.json'
PUBLIC_KEY = 'A63PnxYoXVoZR55xXK9t8zDefh2Shk3oHQuZ39oeu2jF'

with open(PRIVATE_KEY_PATH,'r') as f:
  PRIVATE_KEY = json.load(f)
  PRIVATE_KEY = bytes(PRIVATE_KEY)
  PRIVATE_KEY = base58.b58encode(PRIVATE_KEY)

cfg = {
    "PRIVATE_KEY": PRIVATE_KEY,
    "PUBLIC_KEY": PUBLIC_KEY,
    "DECRYPTION_KEY": SERVER_DECRYPTION_KEY
}
api = MetaplexAPI(cfg)
api_endpoint = "https://api.devnet.solana.com/"

divinity_json_file = "https://arweave.net/lafoms3egQiVeboVVSsgIXRH14DiyxmKLwzD_EWiKv8"
result = api.deploy(api_endpoint, 'test', 'test', 0)
contract_key = json.loads(result).get('contract')
mint_res = api.mint(api_endpoint, contract_key, PUBLIC_KEY, divinity_json_file)