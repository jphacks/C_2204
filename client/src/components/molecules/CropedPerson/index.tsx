import { LegacyRef, useEffect, useRef } from 'react'
import konva from 'konva'
import { Image as RKImage, Transformer } from 'react-konva'
import useImage from 'use-image'

export interface ICropedPersonProps {
  id: string
  imagePath: string
  x: number
  y: number
  width?: number
  height?: number
  isSelected: boolean
  onSelect: () => void
  onChange: (newAttrs: ICropedPersonProps) => void
  hoge?: () => void
}

export const CropedPerson: React.FC<ICropedPersonProps> = (part) => {
  const [image] = useImage(part.imagePath, 'anonymous')
  const imageRef = useRef<konva.Image>(null)
  const trRef: LegacyRef<konva.Transformer> = useRef(null)

  useEffect(() => {
    if (part.isSelected && trRef.current && imageRef.current) {
      trRef.current.nodes([imageRef.current])
    } else {
      trRef.current?.nodes([])
    }
  }, [part.isSelected])

  return (
    <>
      <RKImage
        {...part}
        key={part.id}
        ref={imageRef}
        image={image}
        draggable
        onClick={part.onSelect}
        onTap={part.onSelect}
        onDragEnd={(e) => {
          part.onChange({
            ...part,
            x: e.target.x(),
            y: e.target.y(),
          })
        }}
        onTransformEnd={(e) => {
          const node = imageRef.current
          if (node === null) return
          part.onChange({
            ...part,
            x: node.x(),
            y: node.y(),
          })
        }}
      />
      <Transformer ref={trRef} />
    </>
  )
}
