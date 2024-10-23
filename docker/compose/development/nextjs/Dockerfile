FROM node:18-alpine AS builder
WORKDIR /app

RUN apk add --no-cache --virtual .gyp python3 make g++ && \
    npm install -g pnpm

EXPOSE 3000
ENTRYPOINT ["pnpm", "dev"]
