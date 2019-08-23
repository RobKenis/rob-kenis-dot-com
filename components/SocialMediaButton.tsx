import { FaGithub, FaTwitter, FaLinkedin } from "react-icons/fa";

export const SocialMediaButton = ({ url, icon }) => (
    <a href={url} target={"_blank"}><Icon icon={icon} /></a>
)

const Icon = ({ icon }) => (
    {
        "github": <FaGithub size={"100%"} />,
        "twitter": <FaTwitter size={"100%"} />,
        "linkedin": <FaLinkedin size={"100%"} />
    }[icon]
)