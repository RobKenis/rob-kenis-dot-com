import React from 'react';
import Layout from "../../components/layouts/Layout";
import { LatestPosts } from "../../components/elements/LatestPosts/LatestPosts";

const latestPosts = [
  {
    title: 'Markdown/MDX with Next.js',
    link: '/posts/first_post',
    created: new Date('2021-11-03T00:00:00Z')
  }, {
    title: 'Second post',
    link: '/posts/second_post',
    created: new Date('2021-11-03T00:00:00Z')
  }, {
    title: '3rd post',
    link: '/posts/third_post',
    created: new Date('2021-11-03T00:00:00Z')
  }
];

const Blog = () => (
  <Layout>
    <div className={"container"}>
      <LatestPosts posts={latestPosts}/>
    </div>
  </Layout>
)

export default Blog;
