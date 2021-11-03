import React from "react";
import styles from './LatestPosts.module.css'
import { Avatar, Card } from 'antd';
import Link from 'next/link';

const { Meta } = Card;

interface PostProps {
  title: string;
  link: string;
  created: Date;
}

interface LatestPostsProps {
  posts: PostProps[];
}

const LatestPost: React.FunctionComponent<PostProps> = (props) => (
  <div className={styles.post}>
    <Card
      style={{ width: 300 }}
      cover={
        // eslint-disable-next-line @next/next/no-img-element
        <img
          alt="Cover photo of a kitten"
          src={`https://placekitten.com/450/450?image=${Math.floor(Math.random() * 15) + 1}`}
        />
      }
    >
      <Meta
        avatar={<Avatar src="https://joeschmoe.io/api/v1/random"/>}
        title={<Link href={props.link}>{props.title}</Link>}
        description={props.created.toDateString()}
      />
    </Card>
  </div>
);

export const LatestPosts: React.FunctionComponent<LatestPostsProps> = (props) => (
  <div style={{ display: "flex", flexWrap: 'wrap' }}>
    {props.posts.map(post => (
      <LatestPost key={post.title} title={post.title} link={post.link} created={post.created}/>))}
  </div>
);
