FROM node:20 AS deps

WORKDIR /app

RUN corepack enable && corepack prepare yarn@1.22.22 --activate

RUN npm config set registry https://registry.npmmirror.com \
 && npm config set fetch-retries 5 \
 && npm config set fetch-retry-maxtimeout 120000 \
 && npm config set fetch-retry-mintimeout 20000

COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile


FROM node:20 AS builder

WORKDIR /app

RUN npm config set registry https://registry.npmmirror.com \
 && npm config set fetch-retries 5 \
 && npm config set fetch-retry-maxtimeout 120000 \
 && npm config set fetch-retry-mintimeout 20000

RUN corepack enable && corepack prepare yarn@1.22.22 --activate

COPY --from=deps /app/node_modules ./node_modules
COPY . .

ENV NEXT_TELEMETRY_DISABLED=1
RUN yarn build


FROM node:20 AS runner

WORKDIR /app

ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1

RUN npm config set registry https://registry.npmmirror.com \
 && npm config set fetch-retries 5 \
 && npm config set fetch-retry-maxtimeout 120000 \
 && npm config set fetch-retry-mintimeout 20000

# RUN addgroup -S nodejs && adduser -S nextjs -G nodejs

COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/next.config.ts ./next.config.ts
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules

# USER nextjs

EXPOSE 3300

CMD ["node", "node_modules/next/dist/bin/next", "start", "-p", "3300", "-H", "0.0.0.0"]
