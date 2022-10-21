import Image from 'next/image'
import { SmallRoundedLink } from 'components/atoms/Link'
import type { NextPage } from 'next'

const CreateMemory: NextPage = () => {
  return (
    <div className="flex flex-col items-center h-full w-full">
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
      <div className="absolute text-lg lg:text-2xl mt-20 lg:mt-40">
        どの方法で思い出を作りますか？
      </div>
      <div className="flex flex-col lg:flex-row h-full w-full lg:max-w-screen-lg items-center justify-around my-32">
        <div className="flex justify-center bg-lightAccent text-lightShades w-5/6 lg:w-5/12 h-48 rounded-xl py-2">
          <div className="flex justify-around flex-col w-3/5 pl-4">
            <div className="">
              <p className="pl-4">思い出を賑やかに</p>
            </div>
            <SmallRoundedLink
              color="bg-lightAccent"
              hoverColor="hover:bg-lightAccentHover"
              textColor="text-lightShades"
              href="/memory/add"
            >
              自分の思い出に人を追加
            </SmallRoundedLink>
          </div>
          <div className="relative w-2/5 h-full mr-4">
            <Image
              src="/undraw_group_selfie_re_h8gb.svg"
              layout="fill"
              objectFit="contain"
            />
          </div>
        </div>
        <div className="flex justify-center bg-darkShades text-lightShades w-5/6 lg:w-5/12 h-48 rounded-xl py-2">
          <div className="flex justify-around flex-col w-3/5 pl-4">
            <div className="">
              <p className="pl-4">思い出に入り込む</p>
            </div>
            <SmallRoundedLink
              color="bg-darkShades"
              hoverColor="hover:bg-darkShadesHover"
              textColor="text-lightShades"
              href="/memory/into"
            >
              人の思い出に自分を追加
            </SmallRoundedLink>
          </div>
          <div className="relative w-2/5 h-full mr-4">
            <Image
              src="/undraw_going_offline_ihag.svg"
              layout="fill"
              objectFit="contain"
            />
          </div>
        </div>
      </div>
    </div>
  )
}

export default CreateMemory
