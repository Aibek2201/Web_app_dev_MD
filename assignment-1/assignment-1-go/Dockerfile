FROM golang:1.20 AS builder

WORKDIR /app

COPY . .

RUN go build -o hello-go

FROM alpine:latest

COPY --from=builder /app/hello-go .

CMD ["./hello-go"]
