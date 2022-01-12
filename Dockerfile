FROM golang:alpine

LABEL maintainer="Artem I Benda"

WORKDIR /go/src/app

COPY main.go /go/src/app

RUN go mod init

RUN go build -o helloworld

EXPOSE 6111

CMD ["./helloworld"]
