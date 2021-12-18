solana-keygen new --outfile secret.json > output.txt 2> /dev/null
python account.py
solana airdrop 1 --keypair secret.json > /dev/null