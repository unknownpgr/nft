FROM node:14

WORKDIR /app

RUN yarn add ts-node -g
RUN git clone --branch v1.0.0 https://github.com/metaplex-foundation/metaplex.git ~/metaplex-foundation/metaplex
RUN yarn install --cwd ~/metaplex-foundation/metaplex/js/