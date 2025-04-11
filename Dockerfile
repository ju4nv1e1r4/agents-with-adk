FROM debian-slim-wormbook

WORKDIR /app/

COPY . /app/

CMD [ "uvicorn", "0.0.0.0", "port=8080" ]