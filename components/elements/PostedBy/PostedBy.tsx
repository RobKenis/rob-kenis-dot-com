import React from "react";
import styles from './PostedBy.module.css'
import { Avatar } from "antd";
import { UserOutlined } from "@ant-design/icons";

interface PostedByProps {
  author: string;
  created: Date;
}

export const PostedBy: React.FunctionComponent<PostedByProps> = (props) => (
  <div className={styles.postedBy}>
    <Avatar size={50} icon={<UserOutlined />} />
    <div>
      <strong>{props.author}</strong><br/>
      <small>Posted on {props.created.toDateString()}</small>
    </div>
  </div>
);
