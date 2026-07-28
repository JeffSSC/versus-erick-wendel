FROM golang:1.24-alpine

WORKDIR /app
COPY . .

RUN go build -o server .

ENV PORT=3000
EXPOSE 3000

CMD ["./server"]
