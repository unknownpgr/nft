FROM python:3.8

WORKDIR /app

# Install solana command line tool
RUN sh -c " $( curl -sSfL https://release.solana.com/v1.9.1/install ) "
ENV PATH="/root/.local/share/solana/install/active_release/bin:$PATH"

# Install Node.js environment for Metaplex
RUN apt-get update
RUN apt-get install nodejs -y
RUN apt-get install npm -y
RUN npm cache clean -f
RUN npm install -g n
RUN n stable
RUN npm i ts-node -g
RUN npm install --global yarn

# Install Metaplex CLI
RUN git clone --branch v1.0.0 https://github.com/metaplex-foundation/metaplex.git ~/metaplex-foundation/metaplex
RUN yarn install --cwd ~/metaplex-foundation/metaplex/js/

# Install Metaplex Python API
WORKDIR /
RUN git clone https://github.com/metaplex-foundation/python-api
WORKDIR /python-api
RUN pip install -r requirements.txt
WORKDIR /app

# Set URL to devnet
RUN solana config set --url https://api.devnet.solana.com