docker build -t nft-env .
docker run --rm -it -v $(pwd)/src:/app -w /app nft-env /bin/bash
