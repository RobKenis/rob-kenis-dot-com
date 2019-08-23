import { SocialMediaButton } from "../components/SocialMediaButton";

const socialMedias = {
    "linkedin": "https://linkedin.com/in/robkenis",
    "github": "https://github.com/RobKenis",
    "twitter": "https://twitter.com/RobKenis"
}

export const SocialMediaContainer = () => (
    <div style={{ "display": "flex", "justifyContent": "space-around", "height": "10em" }}>
        {Object.keys(socialMedias).map(social => (<SocialMediaButton icon={social} url={socialMedias[social]} />))}
    </div>
);