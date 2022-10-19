import React, { useState, useEffect } from 'react'

export interface IUserIcon {
  url: string
  size: number
  className?: string
}

export const UserIcon: React.FC<IUserIcon> = ({ url, size, className }) => {
  const [iconUrlState, setIconUrlState] = useState(url)
  useEffect(() => {
    setIconUrlState(url)
  }, [url])
  return (
    <img
      src={iconUrlState}
      className={`h-${size} w-${size} rounded-full object-fill ${className}`}
    />
  )
}
