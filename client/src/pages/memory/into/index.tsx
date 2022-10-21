import { useContext, useState } from 'react'
import { AxiosContext } from 'context/auth'
import { NextPage } from 'next'
import dynamic from 'next/dynamic'
import Image from 'next/image'
import { ImageUrl, PresignedUrl } from 'types'
import { IFileUploadEvent } from 'components/atoms/Button'
const CreateMemoryInto = dynamic(
  () => import('../../../components/organisms/CreateMemoryInto'),
  { ssr: false },
)

const CreateMemoryIntoPage: NextPage = () => {
  const axiosContext = useContext(AxiosContext)
  const [backgroundImageUrl, setBackgroundImageUrl] = useState<string>('')
  const [personImageUrl, setPersonImageUrl] = useState<string>('')

  const inputBackGroundImage = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (!file) return
    const url = URL.createObjectURL(file)
    setBackgroundImageUrl(url)
  }

  const inputPersonImage = async (e: IFileUploadEvent<HTMLInputElement>) => {
    if (!e.target.files?.[0]) return
    if (axiosContext.axios === undefined) return

    const presignedUrl: PresignedUrl = await axiosContext.axios
      .get('/photos/presigned-url')
      .then((res) => res.data)

    const file = e.target.files[0]

    await axiosContext.axios
      .put(presignedUrl.url, file, { headers: { 'Content-Type': file.type } })
      .then((res) => {
        if (res.status >= 400) {
          throw new Error(res.statusText)
        }
      })
      .catch(console.error)

    const cropedPersonImage: ImageUrl = await axiosContext.axios
      .post('/photos/crop', {
        key: presignedUrl.key,
      })
      .then((res) => res.data)

    setPersonImageUrl(cropedPersonImage.url)
  }

  return (
    <div className="">
      {backgroundImageUrl === '' || personImageUrl === '' ? (
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
            <label
              className={`flex items-center justify-center rounded-full ${
                backgroundImageUrl === '' ? 'bg-mainBrand' : 'bg-mainBrandHover'
              } py-1 w-44 cursor-pointer mb-5 hover:bg-mainBrandHover transition-colors shadow-md`}
            >
              <div className="text-lightShades py-1">背景画像を選択</div>
              <input
                type="file"
                accept="image/png"
                className="hidden"
                onChange={inputBackGroundImage}
                disabled={backgroundImageUrl !== ''}
              />
            </label>
            <label
              className={`flex items-center justify-center rounded-full ${
                personImageUrl === '' ? 'bg-mainBrand' : 'bg-mainBrandHover'
              } py-1 w-44 cursor-pointer mb-5 hover:bg-mainBrandHover transition-colors shadow-md`}
            >
              <div className="text-lightShades py-1">あなたの画像を選択</div>
              <input
                type="file"
                accept="image/png"
                className="hidden"
                onChange={inputPersonImage}
                disabled={personImageUrl !== ''}
              />
            </label>
          </div>
        </div>
      ) : (
        <CreateMemoryInto
          backgroundImageUrl={backgroundImageUrl}
          personImageUrl={personImageUrl}
        />
      )}
    </div>
  )
}

export default CreateMemoryIntoPage
