import React from "react";
import { Menu } from "antd";
import { BellOutlined, CodeOutlined, HomeOutlined, MailOutlined } from "@ant-design/icons";
import { Title } from "../Title/Title";
import Link from 'next/link';

interface NavbarProps {
  title: string;
}

export const Navbar: React.FunctionComponent<NavbarProps> = (props) => (
    <Menu mode={"horizontal"}>
      <Menu.Item key={'title'}><Title title={props.title}/></Menu.Item>
      <Menu.Item key={'home'} icon={<HomeOutlined/>} style={{ marginLeft: 'auto' }}><Link href="/">Home</Link></Menu.Item>
      <Menu.Item key={'blog'} icon={<BellOutlined/>}><Link href="/blog">Blog</Link></Menu.Item>
      <Menu.Item key={'learn'} icon={<CodeOutlined/>}><Link href="/learn">Learn</Link></Menu.Item>
      <Menu.Item key={'contact'} icon={<MailOutlined/>}><Link href="/contact">Contact</Link></Menu.Item>
    </Menu>
);
