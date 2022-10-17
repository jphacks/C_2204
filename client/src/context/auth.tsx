import { createContext, useState } from 'react'
import axios, { AxiosInstance, AxiosRequestConfig } from 'axios'
import config from '../config'

export const axiosConfig: AxiosRequestConfig = {
  baseURL: config.API_BASE_URL,
}

export type TAxiosStatus = 'initializing' | 'pending' | 'guest' | 'loggedin'

export interface IAxiosContext {
  axios?: AxiosInstance
  setAuthorizationKey: (key: string) => void
  status: TAxiosStatus
  signout: () => void
  loadingCompleted: (succeed: boolean) => void
  checkAuthKeyValid: () => boolean
}

const AxiosContext = createContext<IAxiosContext>({
  // eslint-disable-next-line @typescript-eslint/no-empty-function
  setAuthorizationKey: () => {},
  status: 'pending',
  // eslint-disable-next-line @typescript-eslint/no-empty-function
  signout: () => {},
  // eslint-disable-next-line @typescript-eslint/no-empty-function
  loadingCompleted: () => {},
  checkAuthKeyValid: () => true,
})

export interface IAxiosProviderProps {
  children: React.ReactNode
}

export const AxiosProvider: React.FC<IAxiosProviderProps> = ({ children }) => {
  const [status, setStatus] = useState<TAxiosStatus>('guest')
  const [authKey, setAuthKey] = useState<string | null>(null)
  const [axiosInstance, setAxiosInstance] = useState<AxiosInstance | undefined>(
    () => axios.create(axiosConfig),
  )

  const setAuthorizationKey = (key: string) => {
    setAuthKey(key)
    setStatus('loggedin')
  }

  const signout = () => {
    setAuthKey(null)
    setStatus('guest')
  }

  const loadingCompleted = (succeed: boolean) => {
    if (succeed) {
      setStatus('loggedin')
    } else {
      setStatus('guest')
    }
  }

  const checkAuthKeyValid = () => false

  const axiosContextValue: IAxiosContext = {
    axios: axiosInstance,
    setAuthorizationKey,
    status,
    signout,
    loadingCompleted,
    checkAuthKeyValid,
  }

  return (
    <AxiosContext.Provider value={axiosContextValue}>
      {children}
    </AxiosContext.Provider>
  )
}
