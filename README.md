# NFT Automation With Solana / Metaplex

The goal of this project is to automate publishing of Non-fungible token (NFT) by dockerizing Metaplex API.

## Project Structure

As you can see in root directory of this repository, there are four main docker images.

- `solana-account` for creating account.
- `solana-airdrop` for geting SOL airdrop.
- `solana-deploy` for publishing NFT. This is the main image.
- `solana-environment` for common environment. Other images are based on this image.

> Don't care about `scripts` directory. That is just some script snippets of Metaplex CLI.

## Instruction

Follow the instructions below to publish an NFT.

1. Run `build-all.sh` script to build all images.
1. Run `docker run --rm solana-account > wallet.json` command to generate wallet.
1. Run `docker run --rm -it -v $(pwd)/wallet.json:/wallet.json:ro solana-airdrop` command to get some SOL coins. If account does not have at least 2 SOLs, it cannot publish NFT. (Actually, `solana-account` image do this internally, but for sure, do it again.)
1. Create a directory for assets. For example, `my-assets`.
1. Add some `png` type images in it. The name of image file will be the name of NFT.
1. Run `docker run --rm -it -v $(pwd)/my-assets:/assets -v $(pwd)/wallet.json:/wallet.json:ro solana-deploy` command to deploy NFT.

Follow the instructions below to check your NFT

1. Add [Phantom wallet](https://phantom.app/) to your browser.
1. Add created wallet to Phantom wallet.
    1. Open `wallet.json` file and copy 'private_key' part, which is a long array of numbers like `[100, 34, 15, ..., 32]`
    1. Click top-left menu at Phantom browser extension.
    1. Click `add/connection wallet` menu.
    1. Click `Import private key` menu.
    1. Paste private key.
1. Then, click collectible menu, (⊞) and you can see the published NFTs.
