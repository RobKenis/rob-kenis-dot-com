import React from "react";
import styles from './Footer.module.css'

interface FooterProps {
  email: string;
}

export const Footer: React.FunctionComponent<FooterProps> = (props) => (
  <div className={styles.footer}>
    <strong>{props.email}</strong>
  </div>
);
