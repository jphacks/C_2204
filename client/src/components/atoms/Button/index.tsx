export interface IButtonProps {
  children: React.ReactNode
  onClick: () => void
  color?:
    | 'lightShades'
    | 'darkShades'
    | 'lightAccent'
    | 'darkAccent'
    | 'mainBrand'
    | 'darkText'
    | 'twitter'
  textColor?:
    | 'lightShades'
    | 'darkShades'
    | 'lightAccent'
    | 'darkAccent'
    | 'mainBrand'
    | 'darkText'
    | 'twitter'
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
      className={`${color ? `bg-${color}` : ''} ${
        textColor ? `text-${textColor}` : ''
      } ${hoverColor ? `hover:bg-${hoverColor}` : ''}
      rounded-full w-48 h-10 flex items-center justify-center shadow-md transition-colors`}
      onClick={onClick}
      type={type}
    >
      {children}
    </button>
  )
}
