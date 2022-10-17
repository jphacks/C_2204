import 'tailwindcss/tailwind.css'
import '../../styles/globals.css'
import { AxiosProvider } from '../context/auth'
import type { AppProps } from 'next/app'

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <AxiosProvider>
      <Component {...pageProps} />
    </AxiosProvider>
  )
}

export default MyApp
