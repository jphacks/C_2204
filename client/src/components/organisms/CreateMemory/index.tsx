import { Fragment, useContext, useEffect, useRef, useState } from 'react'
import { Dialog, Transition } from '@headlessui/react'
import { AxiosContext } from 'context/auth'
import konva from 'konva'
import * as NImage from 'next/image'
import { useRouter } from 'next/router'
import { Image as RKImage, Layer, Stage } from 'react-konva'
import { useWindowSize } from 'react-use'
import { PresignedUrl } from 'types'
import useImage from 'use-image'
import { Button } from 'components/atoms/Button'
import { CropedPerson } from 'components/molecules/CropedPerson'
import type { CropedPersonUrls } from 'types'

interface Part {
  id: string
  imagePath: string
  x: number
  y: number
  isSelected: boolean
}

interface ICreateMemoryProps {
  url: string
}

const CreateMemory: React.FC<ICreateMemoryProps> = ({ url }) => {
  const axiosContext = useContext(AxiosContext)
  const [persons, setPersons] = useState<Part[]>([])
  const [personsPreLoad, setPersonsPreLoad] = useState<Part[]>([])
  const [selectId, setSelectId] = useState<string | null>(null)
  const [backgroundImage] = useImage(url)
  const stageRef = useRef<konva.Stage>(null)
  const layerRef = useRef<konva.Layer>(null)

  const divRef = useRef<HTMLDivElement>(null)
  const { width, height } = useWindowSize()
  const [stageSizeX, setStageSizeX] = useState(0)
  const [stageSizeY, setStageSizeY] = useState(0)
  const scaleX = backgroundImage ? stageSizeX / backgroundImage.width : 1
  const scaleY = backgroundImage ? stageSizeX / backgroundImage.height : 1

  const [isOpen, setIsOpen] = useState(false)
  const openModal = () => setIsOpen(true)
  const closeModal = () => setIsOpen(false)
  const inputRef = useRef<HTMLInputElement>(null)

  const router = useRouter()

  useEffect(() => {
    setStageSizeX(divRef.current?.clientWidth || 0)
  }, [width])
  useEffect(() => {
    setStageSizeY(divRef.current?.clientHeight || 0)
  }, [height])

  useEffect(() => {
    if (axiosContext.axios === undefined) return
    axiosContext.axios
      .get('/photos/persons')
      .then((res) => res.data)
      .then((data: CropedPersonUrls) => {
        const persons: Part[] = data.map((person) => {
          const image = new Image()
          image.crossOrigin = 'anonymous'
          image.src = person.url
          return {
            id: person.key,
            imagePath: person.url,
            image,
            x: 0,
            y: 0,
            isDragging: false,
            isSelected: false,
          }
        })
        setPersonsPreLoad(persons)
      })
  }, [])

  const addPerson = () => {
    if (personsPreLoad.length === 0) return
    const newPerson = personsPreLoad[0]
    setPersonsPreLoad(personsPreLoad.slice(1))
    setPersons([...persons, newPerson])
  }

  const uploadMemory = async () => {
    if (!stageRef.current) return
    if (axiosContext.axios === undefined) return

    const url = stageRef.current.getStage().toDataURL()
    const data = await fetch(url)
      .then((r) => r.blob())
      .then((blobFile) => new File([blobFile], 'image', { type: 'image/png' }))

    const presignedUrl: PresignedUrl = await axiosContext.axios
      .get('/posts/presigned-url')
      .then((res) => res.data)

    await axiosContext.axios
      .put(presignedUrl.url, data, { headers: { 'Content-Type': data.type } })
      .then((res) => {
        if (res.status >= 400) {
          throw new Error(res.statusText)
        }
      })
      .catch(console.error)

    await axiosContext.axios.post('/posts', {
      key: presignedUrl.key,
      body: inputRef.current?.value || '',
    })

    router.push('/timeline')
  }

  const download = () => {
    if (!stageRef.current) {
      return
    }
    const link = document.createElement('a')
    link.download = 'memory.png'
    link.href = stageRef.current.getStage().toDataURL()
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
  }

  const checkDeselect = (
    e: konva.KonvaEventObject<MouseEvent> | konva.KonvaEventObject<TouchEvent>,
  ) => {
    const clickedOnEmpty = e.target === e.target.getStage()
    if (clickedOnEmpty) {
      setSelectId(null)
    }
  }

  const calcStageHeight = () => {
    if (backgroundImage === undefined) return 0
    return (stageSizeX * backgroundImage.height) / backgroundImage.width
  }

  return (
    <>
      <div className="hidden lg:block absolute h-full w-full z-[-1]">
        <NImage.default
          src="/wave-haikei.svg"
          layout="fill"
          objectFit="cover"
        />
      </div>
      <div className="lg:hidden absolute h-full w-full z-[-1]">
        <NImage.default
          src="/wave-haikei-smart-phone.svg"
          layout="fill"
          objectFit="cover"
        />
      </div>
      <div className="flex flex-col w-full h-full items-center justify-center">
        <div
          className="mt-20 w-full h-full max-w-screen-sm lg:max-w-screen-md items-center"
          ref={divRef}
        >
          <Stage
            width={stageSizeX}
            height={calcStageHeight()}
            scaleX={scaleX > 1 ? 1 : scaleX}
            scaleY={scaleX > 1 ? 1 : scaleX}
            ref={stageRef}
            onMouseDown={checkDeselect}
            onTouchStart={checkDeselect}
          >
            <Layer key={'background'}>
              <RKImage image={backgroundImage} />
            </Layer>
            <Layer ref={layerRef}>
              {persons.map((person, i) => (
                <CropedPerson
                  key={person.id}
                  id={person.id}
                  imagePath={person.imagePath}
                  x={person.x}
                  y={person.y}
                  isSelected={person.id === selectId}
                  onSelect={() => {
                    setSelectId(person.id)
                  }}
                  onChange={(newAttrs) => {
                    const newPersons = persons.slice()
                    newPersons[i] = newAttrs
                    setPersons(newPersons)
                  }}
                />
              ))}
            </Layer>
          </Stage>
        </div>
        <div className="mb-20">
          <Button
            color="bg-lightAccent"
            textColor="text-lightShades"
            hoverColor="hover:bg-lightAccentHover"
            onClick={addPerson}
          >
            人を追加
          </Button>
          <div className="mt-5" />
          <Button
            color="bg-mainBrand"
            textColor="text-lightShades"
            hoverColor="hover:bg-mainBrandHover"
            onClick={openModal}
          >
            思い出を投稿する
          </Button>
          <div className="mt-5" />
          <Button
            color="bg-darkShades"
            textColor="text-lightShades"
            hoverColor="hover:bg-darkShadesHover"
            onClick={download}
          >
            画像をダウンロード
          </Button>
        </div>
      </div>
      <Transition appear show={isOpen} as={Fragment}>
        <Dialog as="div" className="relative z-10" onClose={closeModal}>
          <Transition.Child
            as={Fragment}
            enter="ease-out duration-300"
            enterFrom="opacity-0"
            enterTo="opacity-100"
            leave="ease-in duration-200"
            leaveFrom="opacity-100"
            leaveTo="opacity-0"
          >
            <div className="fixed inset-0 bg-black bg-opacity-25" />
          </Transition.Child>
          <div className="fixed inset-0 overflow-y-auto">
            <div className="flex min-h-full items-center justify-center p-4 text-center">
              <Transition.Child
                as={Fragment}
                enter="ease-out duration-300"
                enterFrom="opacity-0 scale-95"
                enterTo="opacity-100 scale-100"
                leave="ease-in duration-200"
                leaveFrom="opacity-100 scale-100"
                leaveTo="opacity-0 scale-95"
              >
                <Dialog.Panel className="w-full max-w-md transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all">
                  <Dialog.Title
                    as="h3"
                    className="flex justify-center font-medium leading-6 text-gray-900"
                  >
                    思い出の説明
                  </Dialog.Title>
                  <div className="mt-2">
                    <input
                      ref={inputRef}
                      type="textarea"
                      className="w-full focus:outline-none focus:ring-2 focus:ring-mainBrand focus:border-transparent border border-gray-300 rounded-md p-2"
                      placeholder="みんなとパーティー！"
                    />
                  </div>

                  <div className="mt-4 flex justify-center">
                    <Button
                      color="bg-mainBrand"
                      textColor="text-lightShades"
                      hoverColor="hover:bg-mainBrandHover"
                      onClick={uploadMemory}
                    >
                      投稿する
                    </Button>
                  </div>
                </Dialog.Panel>
              </Transition.Child>
            </div>
          </div>
        </Dialog>
      </Transition>
    </>
  )
}

export default CreateMemory
