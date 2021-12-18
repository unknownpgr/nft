solana-keygen new --outfile secret.json > output.txt 2> /dev/null
python account.py
solana config set --keypair secret.json > /dev/null
solana airdrop 1 > /dev/null