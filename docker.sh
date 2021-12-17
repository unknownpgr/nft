docker build -t solana-env .
docker run --rm -it -v $(pwd)/src:/app -w /app -p 82:3000 solana-env /bin/bash