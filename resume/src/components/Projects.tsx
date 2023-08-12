import ProjectItem from "./ProjectItem.tsx";
import test_1 from "../assets/test_1.jpg"

const Projects = () => {
    return (
        <div id='projects' className='max-w-[1040px] m-auto md:pl-20 py-16'>
            <h1 className='text-4xl font-bold text-center text-[#001b5e]'>Projects</h1>
            <p className='text-center py-8'>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et
                dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor
                incididunt ut labore dolore magna aliqua.
            </p>
            <div className='grid sm:grid-cols-2 gap-12'>
                <ProjectItem img={test_1} title='Dashboard'/>
                <ProjectItem img={test_1} title='Kanban'/>
                <ProjectItem img={test_1} title='Calendar'/>
                <ProjectItem img={test_1} title='DrivingSchool'/>
            </div>
        </div>
    )
}

export default Projects