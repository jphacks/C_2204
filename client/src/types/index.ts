export interface ImageUrl {
  key: string
  url: string
}

export type CropedPersonUrls = ImageUrl[]

export type PresignedUrl = ImageUrl

export interface PhotosCropRequest {
  key: string
}

export type PhotosCropResponse = CropedPersonUrls

export interface User {
  id: string
  name: string
}

export interface Post {
  photo: ImageUrl
  user: User
  body: string
  created_at: string
  likes: number
  already_like: boolean
}

export type Posts = Post[]

export interface PostRequest {
  key: string
  body: string
}

export type PostsResponse = Posts
