import Layout from "./Layout";
import { Title } from "../elements/Title/Title";
import { Row } from "antd";
import styles from './Post.module.css';
import { PostedBy } from "../elements/PostedBy/PostedBy";
import { CSSProperties } from "react";

const titleCSS: CSSProperties = { fontFamily: 'Lato, serif', margin: '1em 0 2em 0', fontWeight: "bold" }

const Post = ({ meta, children }) => {
  return (
    <Layout>
      <div className={styles.post}>
        <Row>
          <PostedBy author={meta.author} created={meta.created}/>
        </Row>
        <Row>
          <Title title={meta.title} style={titleCSS}/>
        </Row>
        <Row>
          <main className={styles.content}>{children}</main>
        </Row>
      </div>
    </Layout>
  )
}

export default Post;
