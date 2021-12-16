FROM python:3.8

WORKDIR /app

RUN sh -c " $( curl -sSfL https://release.solana.com/v1.9.1/install ) "
RUN export PATH="/root/.local/share/solana/install/active_release/bin:$PATH"

RUN apt-get update
RUN apt-get install nodejs -y
RUN apt-get install npm -y
RUN npm cache clean -f
RUN npm install -g n
RUN n stable

RUN npm install --global yarn
RUN yarn add ts-node -g
RUN git clone --branch v1.0.0 https://github.com/metaplex-foundation/metaplex.git ~/metaplex-foundation/metaplex
RUN yarn install --cwd ~/metaplex-foundation/metaplex/js/
RUN npm i ts-node -g

ENV PATH="/root/.local/share/solana/install/active_release/bin:$PATH"
RUN solana config set --url https://api.devnet.solana.com