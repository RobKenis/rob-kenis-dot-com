import Head from 'next/head';
import { NavBar } from '../components/navbar';
import FontFaceObserver from 'fontfaceobserver';
import React from 'react';

const Fonts = () => {
  const link = document.createElement('link')
  link.href = 'https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,900'
  link.rel = 'stylesheet'

  document.head.appendChild(link)

  const roboto = new FontFaceObserver('Roboto')

  roboto.load().then(() => {
    document.documentElement.classList.add('roboto')
  })
}

class App extends React.Component {
  componentDidMount() {
    Fonts()
  }

  render() {
    return <div>
      <Head>
        <title>Rob Kenis</title>
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
        <link rel="Shortcut Icon" type="image/x-icon" href="favicon.ico" />
      </Head>
      <NavBar />
    </div>
  }
}

export default App;