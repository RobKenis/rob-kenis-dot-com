import React from 'react';
import { Title } from "../../components/elements/Title/Title";
import Layout from "../../components/layouts/Layout";

const Blog = () => (
    <Layout>
      <div className={"container"}>
        <Title title={"Blog."} style={{fontSize: '10vw'}}/>
      </div>
    </Layout>
)

export default Blog;
