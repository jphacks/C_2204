import Image from 'next/image'
import { RoundedLink } from 'components/atoms/Link'
import type { NextPage } from 'next'
import Link from 'next/link'

const Home: NextPage = () => {
  return (
    <div className="bg-lightShades relative overflow-hidden">
      <div className="hidden lg:block absolute h-full w-full">
        <Image src="/wave-haikei.svg" layout="fill" objectFit="cover" />
      </div>
      <div className="lg:hidden absolute h-full w-full">
        <Image
          src="/wave-haikei-smart-phone.svg"
          layout="fill"
          objectFit="cover"
        />
      </div>
      <div className="h-[60px] lg:h-[128px]" />
      <div className="h-[calc(100%-60px)] lg:h-[calc(100%-128px)] lg:flex lg:flex-row-reverse">
        <div className="relative w-3/4 lg:w-1/2 h-1/2 flex items-center justify-center mx-auto lg:mr-[5%]">
          <Image
            src="/undraw_organize_photos_re_ogcy.svg"
            layout="fill"
            objectFit="contain"
            className="translate-y-0"
          />
        </div>
        <div className="relative lg:w-1/2 lg:h-1/2 lg:flex lg:justify-between lg:flex-col">
          <div className="flex justify-center lg:justify-start my-12 lg:ml-[25%] lg:mt-0">
            <span className="text-mainBrand lg:text-lightShades text-3xl lg:text-5xl font-bold">
              Parallel Memory
            </span>
          </div>
          <div className="hidden lg:flex lg:flex-col my-6 lg:mt-0 lg:mb-40 ml-[25%] text-lg text-lightShades">
            <p>自分の思い出をもっとにぎやかにしよう</p>
            <p>人の思い出に入り込もう</p>
            <p>捏造した思い出をみんなと共有しよう</p>
          </div>
          <div className="flex flex-col justify-center lg:justify-start mx-auto mt-40 lg:mt-0 lg:ml-[25%] lg:mb-0">
            <div className="flex flex-col items-center">
              <RoundedLink
                color="bg-mainBrand"
                textColor="text-lightShades"
                hoverColor="hover:bg-mainBrandHover"
                href="/memory"
              >
                思い出を作る
              </RoundedLink>
              <Link href={'/timeline'}>
                <a className="mt-4 text-sm text-mainBrand lg:text-gray-200 hover:underline">
                  みんなの思い出を見る
                </a>
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Home
