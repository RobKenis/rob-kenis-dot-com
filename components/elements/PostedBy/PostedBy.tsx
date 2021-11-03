import React from "react";
import { Avatar } from "antd";

interface PostedByProps {
  author: string;
  created: Date;
}

export const PostedBy: React.FunctionComponent<PostedByProps> = (props) => (
  <div style={{ display: "flex" }}>
    <Avatar size={50} src={'/favicon.ico'} />
    {/*TOP RIGHT BOTTOM LEFT*/}
    <div style={{ margin: '2px 0 0 1em' }}>
      <strong>{props.author}</strong><br/>
      <small>Posted on {props.created.toDateString()}</small>
    </div>
  </div>
);
