FROM solana-env

WORKDIR /app
RUN apt-get update
RUN apt-get install -y jq 
ADD ./src /app
RUN chmod 700 run.sh
ENTRYPOINT ["/bin/bash", "./run.sh" ]