import React from 'react';
import { Title } from "../components/elements/Title/Title";
import Layout from "../components/layouts/Layout";

const App = () => (
  <Layout>
    <div className={"container"}>
      <Title title={"Hi."} fontSize={'10vw'}/>
    </div>
  </Layout>
)

export default App;
