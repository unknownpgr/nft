import json
import os
from pathlib import Path
import sys

ASSET_PATH = '/assets'
WALLET_PATH = '/wallet.json'
COUNT_PATH = '/count'

def get_asset_json(name, image_name, wallet):
  print(name)

  return {
  "name": name,
  "symbol": "",
  "image": image_name,
  "properties": {
    "files": [
      {
        "uri": image_name,
        "type": "image/png"
      }
    ],
    "creators": [
      {
        "address": wallet,
        "share": 100
      }
    ]
  }
}

def generate_asset_json(wallet):
  print('Create NFT of', wallet)

  assets = os.listdir(ASSET_PATH)
  count = 0

  for asset_file_name in assets:
    asset_path =Path(asset_file_name) 
    asset_ext = asset_path.suffix

    if asset_ext!='.png':
      continue

    asset_name = Path(asset_file_name).stem
    asset_json = get_asset_json(asset_name, asset_file_name, wallet)
    with open(os.path.join(ASSET_PATH, f'{asset_name}.json'),'w') as f:
      json.dump(asset_json,f)
    count+=1

  return count

with open(WALLET_PATH) as f:
  wallet = json.load(f)

print('Start minting...')
count = generate_asset_json(wallet['address'])

with open(COUNT_PATH,'w') as f:
  f.write(f'{count}')