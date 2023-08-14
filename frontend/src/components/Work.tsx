import WorkItem from './WorkItem'
import {WorkData} from "../types/WorkData.ts";


const data: WorkData[] = [
    {
        year: 2022,
        title: 'Backend Python Developer @Cloud.ini',
        duration: '1 year 6 months',
        details: 'I undertook a contract position through an umbrella company for Dragonfly Intelligence at Cloud.ini, ' +
            'where my role centered around developing data ingress and process APIs to meet frontend and client needs. ' +
            'Employing a specifications-first approach using OpenAPI 3.0 standards, I focused on creating a robust ' +
            'foundation. Technologies employed encompassed Flask, Connextion, SQLAlchemy, and Pydantic. The project is ' +
            'hosted on the Google Cloud Platform.'

    },
    {
        year: 2022,
        title: 'Fullstack Developer @CodeWithakay',
        duration: 'present',
        details: 'During this period, I embarked on a significant personal project, wholeheartedly dedicating myself to ' +
            'the development of a SaaS product named TheCragStack. This comprehensive Client Management System was ' +
            'meticulously tailored for the indoor climbing center niche. In crafting this system, I engineered the ' +
            'backend using Python-Django and DRF, while the frontend was built upon ReactJS for a seamless user ' +
            'experience. ' +
            'To ensure streamlined deployment, we implemented a robust DevOps strategy, featuring GitLab pipelines ' +
            'hosted on E2C. Furthermore, the application\'s deployment is optimized through AWS services, with the ' +
            'utilization of Docker enhancing its portability and scalability. This comprehensive approach guarantees ' +
            'efficient deployment and optimal performance, facilitating seamless user interactions.'
    },
    {
        year: 2020,
        title: 'Freelance Python Developer @Freelancer/UpWork/Fiverrr',
        duration: '2 years',
        details: 'Over the course of two years as a freelance developer, my primary focus revolved around constructing ' +
            'data acquisition pipelines using a range of Python tools like requests, BeautifulSoup, Selenium, and Scrapy.' +
            ' These technologies facilitated seamless web interactions, while psycopg and SQLAlchemy ensured robust ' +
            'database connections for efficient data handling. I also employed plotly, seaborn, and matplotlib to craft ' +
            'impactful data visualizations. ' +
            'Additionally, I created custom on-demand social media bots for platforms such as Twitter, Instagram, and ' +
            'Discord. By integrating official APIs from these platforms with relevant project-specific APIs, I ' +
            'developed automated solutions that effectively engaged with social media, enhancing user interaction and ' +
            'satisfaction.'
    },
]

const Work = () => {
    return (
        <div id='work' className='max-w-[90%] md:max-w-[1040px] m-auto  md:pl-4 py-16'>
            <h1 className='text-4xl font-bold text-center text-[#001b5e]'>Work</h1>
            {data.map((item: WorkData, idx: number) => (
                <WorkItem
                    key={idx}
                    year={item.year}
                    title={item.title}
                    duration={item.duration}
                    details={item.details}/>
            ))}
        </div>
    )
}

export default Work