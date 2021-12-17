import sys
from os import path
sys.path.append(path.abspath('/python-api'))
import base58
from api.metaplex_api import MetaplexAPI
from cryptography.fernet import Fernet
from solana.keypair import Keypair

account = Keypair()
cfg = {"PRIVATE_KEY": base58.b58encode(account.seed).decode("ascii"), "PUBLIC_KEY": str(account.public_key), "DECRYPTION_KEY": Fernet.generate_key().decode("ascii")}
metaplex = MetaplexAPI(cfg)
wallet = metaplex.wallet()

print(wallet)