import WorkItem from './WorkItem'
import {WorkData} from "../types/WorkData.ts";


const data: WorkData[] = [
    {
        year: 2022,
        title: 'Backend Python Developer @Cloud.ini',
        duration: '1 year 8 months',
        details: 'Contract position via an umbrella company for Dragonfly Intelligence; where my primary focus involves ' +
            'crafting data ingress and process APIs to cater to frontend and client requirements. This project was built with a ' +
            'specs first approach using OpenAPI 3.0 specification standards. Technologies applied: Flask, Connextion, SQLAlchemy ' +
            'Pydantic. Hosted on Google Cloud Platform.'

    },
    {
        year: 2022,
        title: 'Fullstack Developer @CodeWithakay',
        duration: '1 year 7 months',
        details: 'As a large scale personal project I have been working on the development of a SaaS product. ' +
            'TheCragStack is a comprehensive Client Management System with a focus on the indoor climbing centre niche ' +
            'The Backend of the application is being built with Python-Django and DRF; while the Frontend leverages ReactJS ' +
            'The DevOps is utilising GitLab pipelines hosted on E2C'
    },
    {
        year: 2020,
        title: 'Freelance Python Developer @Freelancer/UpWork/Fiverrr',
        duration: '2 years',
        details: 'Primary focus during this period was building data acquisition pipelines powered by various python technologies such as: ' +
            'requests + BeautifulSoup, Selenium, Scrapy for web interactions; psycopg & SQLAlchemy for database connections and interactions ' +
            'plotly, seaborn, matplotlib for data visualization.'
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