FROM node:16-alpine AS deps
WORKDIR /app

RUN apk add --no-cache libc6-compat
COPY ./client/package.json ./client/yarn.lock ./
RUN yarn install --frozen-lockfile

FROM node:16-alpine AS builder
WORKDIR /app

COPY ./client/ .
COPY --from=deps /app/node_modules ./node_modules

RUN yarn build && yarn install --ignore-scripts --prefer-offline

# 本番環境用 --target=runner
FROM node:16-alpine AS runner
WORKDIR /app

ENV NODE_ENV production

RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001

COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

USER nextjs

EXPOSE 3000

CMD ["yarn", "start"]

# 開発環境用 --target=dev
FROM node:16-alpine AS dev
WORKDIR /app

COPY ./client/package.json ./client/yarn.lock ./
RUN yarn install --frozen-lockfile

COPY ./client .

EXPOSE 3000
CMD ["yarn", "dev"]
