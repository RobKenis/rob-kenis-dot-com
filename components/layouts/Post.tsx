import Layout from "./Layout";
import { Title } from "../elements/Title/Title";
import { Col, Row } from "antd";
import { PostedBy } from "../elements/PostedBy/PostedBy";
import { CSSProperties } from "react";

const BREAKPOINT_LG = 8;
const BREAKPOINT_MD = 10;

const titleCSS: CSSProperties = { fontFamily: 'Lato, serif', margin: '1em 0 2em 0', fontWeight: "bold" }

const Post = ({ meta, children }) => {
  return (
    <Layout>
      <Row justify={"center"}>
        <Col lg={BREAKPOINT_LG} md={BREAKPOINT_MD}>
          <PostedBy author={meta.author} created={meta.created}/>
        </Col>
      </Row>
      <Row justify={"center"}>
        <Col lg={BREAKPOINT_LG} md={BREAKPOINT_MD}>
          <Title title={meta.title} style={titleCSS}/>
        </Col>
      </Row>
      <Row justify={"center"}>
        <Col lg={BREAKPOINT_LG} md={BREAKPOINT_MD}>
          <main>{children}</main>
        </Col>
      </Row>
    </Layout>
  )
}

export default Post;
