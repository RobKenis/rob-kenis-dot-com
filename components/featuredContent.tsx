import CSS from 'csstype';

const containerStyle: CSS.Properties = {
  display: 'flex',
  justifyContent: 'center',
  fontFamily:'Oswald',
}

const FeaturedContent = () => (<div style={containerStyle}><p>Have a look at <a href="https://spunt.be">spunt.be</a> while this site is being built.</p></div>)

export default FeaturedContent;