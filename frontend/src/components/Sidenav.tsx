import {useState} from "react";
import {AiOutlineMenu, AiOutlineHome, AiOutlineProject, AiOutlineMail} from "react-icons/ai";
import {GrProjects} from "react-icons/gr";
import {BsPerson} from "react-icons/bs";
import {TooltipComponent} from "@syncfusion/ej2-react-popups"

const Sidenav = () => {
    const [nav, setNav] = useState(false)
    const handleNav = () => {
        setNav(!nav);
    };

    const MenuItemWithTooltip: React.FC<{
        content: string;
        icon: React.ReactNode;
        link: string;
    }> = ({content, icon, link}) => (
        <TooltipComponent content={content} openDelay={300} position="RightCenter">
            <a
                onClick={handleNav}
                href={link}
                className="rounded-full shadow-lg bg-gray-100 shadow-gray-400 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-200"
            >
                {icon}
            </a>
        </TooltipComponent>
    );

    return (
        <div className='relative'>
            <AiOutlineMenu onClick={handleNav} className='fixed top-4 right-4 z-[99] md:hidden'/>
            {
                nav ? (
                        <div className='fixed w-full h-screen bg-white/70 flex flex-col justify-center items-center z-20'>
                            <a onClick={handleNav} href='#main'
                               className='w-[75%] flex justify-center items-center rounded-full shadow-lg bg-gray-100 shadow-gray-400 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-200'
                            >
                                <AiOutlineHome size={20}/>
                                <span className='pl-4'>Home</span>
                            </a>
                            <a onClick={handleNav} href='#profile'
                               className='w-[75%] flex justify-center items-center rounded-full shadow-lg bg-gray-100 shadow-gray-400 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-200'>
                                <BsPerson size={20}/>
                                <span className='pl-4'>Profile</span>
                            </a>
                            <a onClick={handleNav} href='#work'
                               className='w-[75%] flex justify-center items-center rounded-full shadow-lg bg-gray-100 shadow-gray-400 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-200'>
                                <AiOutlineProject size={20}/>
                                <span className='pl-4'>Work</span>
                            </a>
                            <a onClick={handleNav} href='#projects'
                               className='w-[75%] flex justify-center items-center rounded-full shadow-lg bg-gray-100 shadow-gray-400 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-200'>
                                <GrProjects size={20}/>
                                <span className='pl-4'>Projects</span>
                            </a>
                            <a onClick={handleNav} href='#contact'
                               className='w-[75%] flex justify-center items-center rounded-full shadow-lg bg-gray-100 shadow-gray-400 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-200'>
                                <AiOutlineMail size={20}/>
                                <span className='pl-4'>Contact</span>
                            </a>
                        </div>
                    )
                    : (
                        ''
                    )
            }
            {/*TODO add tooltip */}
            <AiOutlineMenu onClick={handleNav} className="fixed top-4 right-4 z-[99] md:hidden"/>
            {nav ? (
                <div className="fixed w-full h-screen bg-white/70 flex flex-col justify-center items-center z-20">
                    <MenuItemWithTooltip content="Home" icon={<AiOutlineHome size={20}/>} link="#main"/>
                    <MenuItemWithTooltip content="Profile" icon={<BsPerson size={20}/>} link="#profile"/>
                    <MenuItemWithTooltip content="Work" icon={<AiOutlineProject size={20}/>} link="#work"/>
                    <MenuItemWithTooltip content="Projects" icon={<GrProjects size={20}/>} link="#projects"/>
                    <MenuItemWithTooltip content="Contact" icon={<AiOutlineMail size={20}/>} link="#contact"/>
                </div>
            ) : (
                ""
            )}
            <div className='md:block hidden fixed top-[25%] z-10'>
                <div className='flex flex-col'>
                    <a href='#main'
                       className='rounded-full shadow-lg bg-gray-100 shadow-gray-400 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-200'>
                        <TooltipComponent content='Home' position='RightCenter'>
                            <AiOutlineHome size={20}/>
                        </TooltipComponent>
                    </a>
                    <a href='#profile'
                       className='rounded-full shadow-lg bg-gray-100 shadow-gray-400 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-200'>
                        <TooltipComponent content='Profile' position='RightCenter'>
                            <BsPerson size={20}/>
                        </TooltipComponent>
                    </a>
                    <a href='#work'
                       className='rounded-full shadow-lg bg-gray-100 shadow-gray-400 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-200'>
                        <TooltipComponent content='Work' position='RightCenter'>
                            <AiOutlineProject size={20}/>
                        </TooltipComponent>
                    </a>
                    <a href='#projects'
                       className='rounded-full shadow-lg bg-gray-100 shadow-gray-400 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-200'>
                        <TooltipComponent content='Projects' position='RightCenter'>
                            <GrProjects size={20}/>
                        </TooltipComponent>
                    </a>
                    <a href='#contact'
                       className='rounded-full shadow-lg bg-gray-100 shadow-gray-400 m-2 p-4 cursor-pointer hover:scale-110 ease-in duration-200'>
                        <TooltipComponent content='Contact' position='RightCenter'>
                            <AiOutlineMail size={20}/>
                        </TooltipComponent>
                    </a>
                </div>
            </div>
        </div>
    )
}

export default Sidenav