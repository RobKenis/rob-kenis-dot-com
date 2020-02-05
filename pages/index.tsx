import Head from 'next/head';
import { NavBar } from '../components/navbar';
import FontFaceObserver from 'fontfaceobserver';
import React from 'react';
import FeaturedContent from '../components/featuredContent';

const Fonts = () => {
  const fonts = ['Roboto', 'Oswald'];

  fonts.forEach(font =>  {
    const link = document.createElement('link')
    link.href = `https://fonts.googleapis.com/css?family=${font}:300,400,500,700,900`
    link.rel = 'stylesheet'
  
    document.head.appendChild(link)
  
    const roboto = new FontFaceObserver(font)
  
    roboto.load().then(() => {
      document.documentElement.classList.add(font.toLowerCase())
    })
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
      <FeaturedContent/>
    </div>
  }
}

export default App;