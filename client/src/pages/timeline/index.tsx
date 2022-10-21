import { useContext, useEffect, useState } from 'react'
import { AxiosContext } from 'context/auth'
import { NextPage } from 'next'
import { Posts } from 'types'
import { RoundedLink } from 'components/atoms/Link'
import { UserPosts } from 'components/organisms/Photos'

const Timeline: NextPage = () => {
  const [posts, setPosts] = useState<Posts>([])
  const axiosContext = useContext(AxiosContext)

  useEffect(() => {
    if (axiosContext.axios === undefined) return
    axiosContext.axios.get('/posts').then((res) => setPosts(res.data))
  }, [])

  return (
    <div>
      <div className="flex flex-col items-center h-full pt-4 lg:pt-4">
        <div className="flex flex-col justify-center w-full lg:max-w-screen-md">
          <div>
            {posts.length ? (
              <UserPosts {...posts} />
            ) : (
              <>
                <div className="flex justify-center bg-lightShades items-center text-darkText rounded-xl h-24 lg:rounded-xl lg:shadow-lg">
                  <div>みんなの撮った写真がここに表示されます</div>
                </div>
              </>
            )}
          </div>
        </div>
      </div>
      <div className="fixed right-5 bottom-5 z-1">
        <RoundedLink
          href="/memory"
          color="bg-mainBrand"
          hoverColor="hover:bg-mainBrandHover"
          textColor="text-lightShades"
        >
          思い出を作る
        </RoundedLink>
      </div>
    </div>
  )
}

export default Timeline
