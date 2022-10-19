export interface IButtonProps {
  children: React.ReactNode
  onClick: () => void
  color?:
    | 'bg-lightShades'
    | 'bg-darkShades'
    | 'bg-lightAccent'
    | 'bg-darkAccent'
    | 'bg-mainBrand'
    | 'bg-darkText'
    | 'bg-twitter'
  textColor?:
    | 'text-lightShades'
    | 'text-darkShades'
    | 'text-lightAccent'
    | 'text-darkAccent'
    | 'text-mainBrand'
    | 'text-darkText'
    | 'text-twitter'
  hoverColor?: string
  type?: 'button' | 'submit' | 'reset'
}

export interface IPhotoUploadProps {
  photoId: string
}

export interface ITwitterAuthorizationResponse {
  url: string
  oauth_token: string
  oauth_token_secret: string
}

export interface IFileUploadEvent<T = EventTarget> {
  target: T
}

export const Button: React.FC<IButtonProps> = ({
  children,
  onClick,
  color,
  textColor,
  hoverColor,
  type,
}) => {
  return (
    <button
      className={`${color ? color : ''} ${textColor ? textColor : ''} ${
        hoverColor ? hoverColor : ''
      }
      rounded-full w-48 h-10 flex items-center justify-center shadow-md transition-colors`}
      onClick={onClick}
      type={type}
    >
      {children}
    </button>
  )
}

export const ButtonSmall: React.FC<IButtonProps> = ({
  children,
  onClick,
  color,
  textColor,
  hoverColor,
  type,
}) => {
  return (
    <button
      className={`${color ? color : ''} ${textColor ? textColor : ''} ${
        hoverColor ? hoverColor : ''
      }
      rounded-full w-40 h-8 text-xs flex items-center justify-center shadow-md transition-colors`}
      onClick={onClick}
      type={type}
    >
      {children}
    </button>
  )
}
