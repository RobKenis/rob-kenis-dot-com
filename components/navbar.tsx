import CSS from 'csstype';

import { Icon } from 'antd';

const containerStyle: CSS.Properties = {
  display: 'flex',
  justifyContent: 'space-around'
}

const linkStyle: CSS.Properties = {
  fontSize: '2em'
}

const links = [
  {icon: 'github', url: 'https://github.com/RobKenis/'},
  {icon: 'twitter', url: 'https://twitter.com/RobKenis/'},
  {icon: 'linkedin', url: 'https://linkedin.com/in/robkenis/'},
]

export const NavBar = () => (<div style={containerStyle}>
  {links.map((link, index) => (<a key={index} href={link.url} target="_blank" rel="noopener" style={linkStyle}><Icon type={link.icon}/></a>))}
</div>);