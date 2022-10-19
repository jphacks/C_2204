import Link from 'next/link'

export interface IRoundedLinkProps {
  children?: React.ReactNode
  href: string
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
}

export const RoundedLink: React.FC<IRoundedLinkProps> = ({
  children,
  href,
  color,
  textColor,
  hoverColor,
}) => (
  <div>
    <Link href={{ pathname: href }}>
      <a
        className={`${color} ${textColor} ${hoverColor} text-lightShades hover:bg-mainBrandHover rounded-full w-48 h-10 flex items-center justify-center shadow-md transition-colors`}
      >
        {children}
      </a>
    </Link>
  </div>
)

export const SmallRoundedLink: React.FC<IRoundedLinkProps> = ({
  children,
  href,
  color,
  textColor,
  hoverColor,
}) => (
  <div>
    <Link href={{ pathname: href }}>
      <a
        className={`${color} ${textColor} ${hoverColor} rounded-full w-40 h-8 text-xs flex items-center justify-center shadow-md transition-colors`}
      >
        {children}
      </a>
    </Link>
  </div>
)
