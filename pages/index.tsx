import Head from 'next/head';
import React from 'react';
import { Layout, Empty } from 'antd';
const { Header, Footer, Content } = Layout;

import '../css/antd.less'
import { NavBar } from '../components/navbar';

const App = () => (
  <div>
    <Head>
      <title>Rob Kenis</title>
      <meta name="viewport" content="initial-scale=1.0, width=device-width" />
      <link rel="Shortcut Icon" type="image/x-icon" href="favicon.ico" />
    </Head>
    <Layout>
      <Header><NavBar/></Header>
      <Content style={{padding: '2em'}}><Empty/></Content>
      <Footer style={{display: 'flex', justifyContent: 'center'}}>Rob Kenis ©2020</Footer>
    </Layout>
  </div>
)

export default App;