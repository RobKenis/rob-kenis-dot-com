import Head from 'next/head';
import { SocialMediaContainer } from '../components/SocialMediaContainer';

const Index = () => (
  <div>
    <Head>
      <title>Rob Kenis</title>
      <meta name="viewport" content="initial-scale=1.0, width=device-width" />
      <link rel="Shortcut Icon" type="image/x-icon" href="static/assets/avatar.ico" />
    </Head>
    <div style={{ "display": "flex", "flexDirection": "column", "justifyContent": "center", "height": "95vh" }}>
      <SocialMediaContainer />
    </div>
  </div>
)

export default Index;