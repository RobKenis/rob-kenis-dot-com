import Head from 'next/head';
import { NavBar } from '../components/navbar';
import React from 'react';
import FeaturedContent from '../components/featuredContent';

import '../css/antd.less'

const App = () => (
  <div>
    <Head>
      <title>Rob Kenis</title>
      <meta name="viewport" content="initial-scale=1.0, width=device-width" />
      <link rel="Shortcut Icon" type="image/x-icon" href="favicon.ico" />
    </Head>
    <NavBar />
    <FeaturedContent />
  </div>
)

export default App;