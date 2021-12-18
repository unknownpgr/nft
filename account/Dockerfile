FROM solana-env

WORKDIR /app
ADD ./src /app
RUN chmod 700 ./run.sh
CMD [ "/bin/bash", "run.sh" ]