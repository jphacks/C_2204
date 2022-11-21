export default {
  BASE_URL: process.env.NEXT_PUBLIC_BASE_URL || '',
  S3_IMG_BUCKET_ENDPOINT: process.env.NEXT_PUBLIC_S3_IMG_BUCKET_ENDPOINT || '',
  API_BASE_URL:
    process.env.NEXT_PUBLIC_API_BASE_URL || 'https://parallel-memory.ls.datech.jp/api',
}
