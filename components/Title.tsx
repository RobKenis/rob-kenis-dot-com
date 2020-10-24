import React from "react";

interface TitleProps {
  title: string;
}

export const Title: React.FunctionComponent<TitleProps> = (props) => (<h1>{props.title}</h1>);
