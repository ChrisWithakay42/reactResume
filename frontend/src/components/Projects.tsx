import ProjectItem from "./ProjectItem.tsx";
import test_1 from "../assets/test_1.jpg"

const Projects = () => {
    return (
        <div id='projects' className='max-w-[90%] md:max-w-[1040px] m-auto  md:pl-4 py-16'>
            <h1 className='text-4xl font-bold text-center text-[#001b5e]'>Projects</h1>
            <p className='text-center py-8'>
               Check out some of my work. All these applications are powered by ReactJS on the frontend and some kind of a
                Python framework on the back end. Mostly Flask, maybe Django and in the near future I will add in some Go
                projects I have been working on.
            </p>
            <div className='grid sm:grid-cols-2 gap-12'>
                <ProjectItem img={test_1} title='Dashboard' stack={'ReactJS/Flask'}/>
                <ProjectItem img={test_1} title='Kanban' stack={'ReactJS/Flask'}/>
                <ProjectItem img={test_1} title='Calendar' stack={'ReactJS/Django'}/>
                <ProjectItem img={test_1} title='User Form' stack={'ReactJS/Go'}/>
            </div>
        </div>
    )
}

export default Projects