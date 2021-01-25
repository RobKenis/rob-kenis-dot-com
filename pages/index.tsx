import Head from 'next/head';
import React from 'react';
import {Title} from "../components/Title";

const App = () => (
  <div>
    <Head>
      <title>Rob Kenis</title>
      <meta name="viewport" content="initial-scale=1.0, width=device-width" />
      <link rel="Shortcut Icon" type="image/x-icon" href="favicon.ico" />
    </Head>
    <div className={"container"}>
      <Title title={"Hi."}/>
    </div>
  </div>
)

export default App;
