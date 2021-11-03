import styles from './Title.module.css'

import React from "react";

interface TitleProps {
  title: string;
  fontSize?: string;
}

export const Title: React.FunctionComponent<TitleProps> = (props) => (
  <h1 style={{fontSize: props.fontSize}} className={styles.title}>{props.title}</h1>
);
