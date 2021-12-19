#!/bin/bash

python deploy.py
cat /wallet.json | jq -c .private_key > /config.json

metaplex=~/metaplex-foundation/metaplex/js/packages/cli/src/candy-machine-cli.ts

ts-node $metaplex upload /assets --env devnet --keypair /config.json
ts-node $metaplex create_candy_machine --env devnet --keypair /config.json -p 1

for i in {1..$(cat /count)}
do
  ts-node $metaplex mint_one_token -k /config.json --env devnet
done

