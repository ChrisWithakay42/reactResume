import {TypeAnimation} from 'react-type-animation'
import {FaGithub} from "react-icons/fa";
import {FaLinkedinIn} from "react-icons/fa6";


const Main = () => {
    return (
        <div id='main'>
            <img alt='Backgroud-image' className='w-full h-screen object-cover object-left'
                 src='https://images.unsplash.com/photo-1453928582365-b6ad33cbcf64?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2073&q=80'/>
            <div className='w-full h-screen absolute top-0 bg-white/50'>
                <div className='max-w-[700px] m-auto h-full flex flex-col justify-center lg:items-start items-center'>
                    <h1 className='sm:text-5xl text-4xl font-bold text-gray-800'>Hello Friend! My name is Kris.</h1>
                    <h2 className='flex sm:text-3xl text-2xl pt-4 text-gray-800'>
                        I'm a
                        <TypeAnimation
                            sequence={[
                                // Same substring at the start will only be typed out once, initially
                                'Coder.',
                                2000,
                                'Developer.',
                                2000,
                                'Tech Enthusiast.',
                                2000
                            ]}
                            wrapper="div"
                            cursor={true}
                            repeat={Infinity}
                            speed={50}
                            style={{fontSize: '1em', paddingLeft: '5px'}}
                        />
                    </h2>
                    <div className='flex justify-between pt-6 max-w-[200px] w-full'>
                        <FaGithub className='cursor-pointer' size={20}/>
                        <FaLinkedinIn className='cursor-pointer' size={20}/>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Main