import {Navbar} from '../elements/Navbar/Navbar';
import Head from "next/head";
import React from "react";

export default function Layout({children}) {
  return (
    <>
      <Head>
        <title>Rob Kenis</title>
        <meta name="viewport" content="initial-scale=1.0, width=device-width"/>
        <link rel="Shortcut Icon" type="image/x-icon" href="favicon.ico"/>
      </Head>
      <Navbar title={"Rob Kenis"}/>
      <main>{children}</main>
    </>
  )
}
