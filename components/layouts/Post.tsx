const Post = ({ meta, children }) => {
  return (
    <>
      <h1>{meta.title}</h1>
      <main>{children}</main>
    </>
  )
}

export default Post;
