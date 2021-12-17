docker build -t nft-env .
docker run --rm -it -v $(pwd)/src:/app -w /app -p 82:3000 nft-env /bin/bash