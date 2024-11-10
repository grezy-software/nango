FROM node:18-alpine AS builder
WORKDIR /app

COPY ./frontend .
RUN apk add --no-cache --virtual .gyp python3 make g++ && \
    npm install -g pnpm

EXPOSE 3000
COPY ./docker/compose/development/nextjs/start.sh /start.sh
RUN chmod +x /start.sh
CMD /start.sh
