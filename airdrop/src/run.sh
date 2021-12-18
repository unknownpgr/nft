cat /wallet.json | jq -c .private_key > config.json
solana airdrop 2 --keypair config.json