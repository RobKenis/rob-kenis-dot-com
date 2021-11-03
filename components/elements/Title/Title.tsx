import styles from './Title.module.css'

import React, { CSSProperties } from "react";

interface TitleProps {
  title: string;
  style?: CSSProperties;
}

export const Title: React.FunctionComponent<TitleProps> = (props) => (
  <h1 style={props.style} className={styles.title}>{props.title}</h1>
);
