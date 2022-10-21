import React, { useContext, useEffect, Fragment } from 'react'
import { faTimesCircle } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { Dialog, Transition } from '@headlessui/react'
import { AxiosContext } from 'context/auth'
import Link from 'next/link'
import { Post, Posts } from 'types'

export const UserPost: React.FC<{ post: Post }> = ({ post }) => {
  const axiosContext = useContext(AxiosContext)
  const [url, setUrl] = React.useState<string>(post.photo.url)
  const [isOpen, setIsOpen] = React.useState<boolean>(false)

  const openModal = () => {
    setIsOpen(true)
  }
  const closeModal = () => {
    setIsOpen(false)
  }

  useEffect(() => {
    setUrl(post.photo.url)
  }, [post.photo.url])

  return (
    <div className="flex flex-col items-center bg-lightShades mt-2 lg:mb-4 lg:rounded-xl lg:shadow-lg">
      {post.body ? (
        <div className="self-start mx-4 lg:mx-28 my-5 px-4 lg:text-lg">
          {post.body}
        </div>
      ) : (
        <div className="mt-5" />
      )}
      <div className="flex relative w-full justify-center mb-8 cursor-pointer hover:opacity-80">
        <img
          src={url}
          alt="photo"
          className="h-52 md:h-72 w-5/6 max-w-lg object-cover rounded-2xl absolute z-0 align-top filter blur-md"
          onClick={openModal}
        />
        <img
          src={url}
          alt="photo"
          className="h-52 md:h-72 w-5/6 max-w-lg object-cover rounded-2xl drop-shadow relative"
          onClick={openModal}
        />
      </div>
      <Transition
        appear
        show={isOpen}
        as={Fragment}
        enter="transition duration-100 ease-out"
        enterFrom="transform scale-95 opacity-0"
        enterTo="transform scale-100 opacity-100"
        leave="transition duration-75 ease-out"
        leaveFrom="transform scale-100 opacity-100"
        leaveTo="transform scale-95 opacity-0"
      >
        <Dialog
          as="div"
          className="flex items-center justify-center fixed inset-0 z-10 overflow-y-auto"
          onClose={closeModal}
        >
          <Dialog.Overlay className="fixed inset-0 bg-black opacity-50" />
          <button
            onClick={closeModal}
            className="flex items-center justify-center bg-black-500 absolute top-0 left-0 m-4 lg:m-8"
          >
            <FontAwesomeIcon
              icon={faTimesCircle}
              className="text-lightShades text-xl lg:text-3xl absolute z-0 rounded-full"
            />
          </button>
          <img
            src={url}
            alt="photo"
            className="w-11/12 max-w-full max-h-11/12 object-contain absolute z-0 my-14"
            onClick={closeModal}
          />
        </Dialog>
      </Transition>
    </div>
  )
}

export const UserPosts: React.FC<Posts> = (photoProp) => {
  const [photos, setPhotos] = React.useState<Posts>(photoProp)
  useEffect(() => {
    setPhotos(photoProp)
  }, [photoProp])

  return (
    <div className="bg-gray-100 lg:bg-transparent pb-20">
      {Object.entries(photos).map(([s, p], _) => {
        return <UserPost key={p.photo.url} post={p} />
      })}
    </div>
  )
}
