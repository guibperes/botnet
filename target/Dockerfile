FROM node:12-alpine

WORKDIR /app

COPY package*.json ./

RUN npm ci

COPY . .

CMD ["node", "src/server.js"]
