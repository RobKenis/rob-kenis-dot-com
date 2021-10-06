import styles from './Title.module.css'

import React from "react";

interface TitleProps {
  title: string;
}

export const Title: React.FunctionComponent<TitleProps> = (props) => (
  <h1 className={styles.title}>{props.title}</h1>
);
