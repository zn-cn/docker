FROM golang:1.10

WORKDIR /app
COPY . .

ENV GOPATH "/app"
RUN go build -o bin/main src/main.go && rm -rf src
EXPOSE 1323

ENTRYPOINT [ "bin/main" ]   