import CSS from 'csstype';

const navStyle: CSS.Properties = {
  display: 'flex',
  justifyContent: 'space-evenly',
  alignItems: 'center',
  flexWrap: 'wrap'
}

const homeButtonStyle: CSS.Properties = {
  fontFamily: 'Roboto',
  fontWeight: 'bold',
  fontSize: '2em'
}

const internalLinksStyle: CSS.Properties = {
  display: 'flex',
  justifyContent: 'space-between',
  width: '25%',
}

const internalLinkStyle: CSS.Properties = {
  textDecoration: 'none',
  color: 'gray',
  fontSize: '1.2em'
}

const socialMediaButtonsStyle: CSS.Properties = {
  display: 'flex',
  justifyContent: 'space-around',
  width: '15%',
}

const SocialIconStyle: CSS.Properties = {
  width: '2em',
  height: '2em'
}

export const NavBar = () => (<nav style={navStyle}>
  <HomeButton />
  <InternalLinks />
  <SocialMediaButtons />
</nav>);

const HomeButton = () => (<div style={homeButtonStyle}>Rob Kenis</div>);

const internalLinksData = [{ title: 'AWS', href: 'https://aws.axxes.com' }, { title: 'Blog', href: 'https://aws.axxes.com' }, { title: 'S.', href: 'https://spunt.be' }];

const InternalLinks = () => (<div style={internalLinksStyle}>
  {internalLinksData.map((link, index) => (<a key={index} style={internalLinkStyle} href={link.href} target="_blank" rel="noopener">{link.title}</a>))}
</div>)

const SocialMediaButtons = () => (<div style={socialMediaButtonsStyle}>
 <a href="https://github.com/RobKenis" target="_blank" rel="noopener"><GitHubIcon/></a>
 <a href="https://twitter.com/RobKenis" target="_blank" rel="noopener"><TwitterIcon/></a>
</div>);

const GitHubIcon = () => (<svg style={SocialIconStyle} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 17 16" fill="none" ><g clipPath="url(githublogo)" ><path fill="currentColor" fillRule="evenodd" d="M8.18391.249268C3.82241.249268.253906 3.81777.253906 8.17927c0 3.46933 2.279874 6.44313 5.451874 7.53353.3965.0991.49563-.1983.49563-.3965v-1.3878c-2.18075.4956-2.67638-.9912-2.67638-.9912-.3965-.8922-.89212-1.1895-.89212-1.1895-.69388-.4957.09912-.4957.09912-.4957.793.0992 1.1895.793 1.1895.793.69388 1.2887 1.88338.8922 2.27988.6939.09912-.4956.29737-.8921.49562-1.0904-1.78425-.1982-3.5685-.8921-3.5685-3.96496 0-.89212.29738-1.586.793-2.08162-.09912-.19825-.3965-.99125.09913-2.08163 0 0 .69387-.19825 2.18075.793.59475-.19825 1.28862-.29737 1.9825-.29737.69387 0 1.38775.09912 1.98249.29737 1.4869-.99125 2.1808-.793 2.1808-.793.3965 1.09038.1982 1.88338.0991 2.08163.4956.59475.793 1.28862.793 2.08162 0 3.07286-1.8834 3.66766-3.66764 3.86586.29737.3965.59474.8921.59474 1.586v2.1808c0 .1982.0991.4956.5948.3965 3.172-1.0904 5.4518-4.0642 5.4518-7.53353-.0991-4.3615-3.6676-7.930002-8.02909-7.930002z" clipRule="evenodd" ></path></g><defs ><clipPath id="githublogo"><path fill="transparent" d="M0 0h15.86v15.86H0z" transform="translate(.253906 .0493164)" ></path></clipPath></defs></svg>);
const TwitterIcon = () => (<svg style={SocialIconStyle} viewBox="0 0 24 24"><g><path d="M23.643 4.937c-.835.37-1.732.62-2.675.733.962-.576 1.7-1.49 2.048-2.578-.9.534-1.897.922-2.958 1.13-.85-.904-2.06-1.47-3.4-1.47-2.572 0-4.658 2.086-4.658 4.66 0 .364.042.718.12 1.06-3.873-.195-7.304-2.05-9.602-4.868-.4.69-.63 1.49-.63 2.342 0 1.616.823 3.043 2.072 3.878-.764-.025-1.482-.234-2.11-.583v.06c0 2.257 1.605 4.14 3.737 4.568-.392.106-.803.162-1.227.162-.3 0-.593-.028-.877-.082.593 1.85 2.313 3.198 4.352 3.234-1.595 1.25-3.604 1.995-5.786 1.995-.376 0-.747-.022-1.112-.065 2.062 1.323 4.51 2.093 7.14 2.093 8.57 0 13.255-7.098 13.255-13.254 0-.2-.005-.402-.014-.602.91-.658 1.7-1.477 2.323-2.41z"></path></g></svg>);