import { useState } from 'react'
import { NextPage } from 'next'
import dynamic from 'next/dynamic'
import Image from 'next/image'
const CreateMemory = dynamic(
  () => import('../../../components/organisms/CreateMemory'),
  { ssr: false },
)

const CreateMemoryAddPage: NextPage = () => {
  const [url, setUrl] = useState<string>('')

  const inputBackGroundImage = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (!file) return
    const url = URL.createObjectURL(file)
    setUrl(url)
  }

  return (
    <div className="">
      {url === '' ? (
        <div className="flex flex-col items-center w-full h-full">
          <div className="hidden lg:block absolute h-full w-full z-[-1]">
            <Image
              src="/layered-waves-haikei.svg"
              layout="fill"
              objectFit="cover"
            />
          </div>
          <div className="lg:hidden absolute h-full w-full z-[-1]">
            <Image
              src="/layered-waves-haikei-smart-phone.svg"
              layout="fill"
              objectFit="cover"
            />
          </div>
          <div className="relative w-4/5 h-1/2 md:w-1/2 xl:w-1/3">
            <Image
              src="/undraw_posting_photo_re_plk8.svg"
              layout="fill"
              objectFit="contain"
            />
          </div>
          <div className="flex flex-col h-1/2 items-center">
            <p className="my-5 lg:mb-10 lg:text-lg">
              さっそく思い出を作りましょう!
            </p>
            <label className="flex items-center justify-center rounded-full bg-mainBrand py-1 w-44 cursor-pointer mb-24 hover:bg-mainBrandHover transition-colors shadow-md">
              <div className="text-lightShades py-1">背景画像を選択</div>
              <input
                type="file"
                accept="image/png"
                className="hidden"
                onChange={inputBackGroundImage}
              />
            </label>
          </div>
        </div>
      ) : (
        <CreateMemory url={url} />
      )}
    </div>
  )
}

export default CreateMemoryAddPage
