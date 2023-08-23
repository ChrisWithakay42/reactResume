import {TypeAnimation} from 'react-type-animation'
import {FaGithub} from "react-icons/fa";
import {FaLinkedinIn} from "react-icons/fa6";
import main from "../assets/main.jpg"

// src='https://images.unsplash.com/photo-1453928582365-b6ad33cbcf64?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2073&q=80'
// src='https://images.unsplash.com/photo-1606229365485-93a3b8ee0385?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=774&q=80'

const Main = () => {
    return (
        <div id='main' className='relative h-screen'>
            <img
                className='absolute w-full h-full object-cover object-left scale-x-[-1]'
                src={main}
                alt='Background-image'
            />
            <div className='absolute inset-0 flex justify-center items-center bg-white bg-opacity-50'>
                <div className='p-6 text-center rounded-lg'>
                    <h1 className='text-4xl font-bold text-gray-800'>Hi! My name is Kris;</h1>
                    <h2 className='text-2xl pt-4 text-gray-800'>
                        I'm a
                        <TypeAnimation
                            sequence={[
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
                    <div className='pt-6'>
                        <a href='https://github.com/ChrisWithakay42' target='_blank'>
                            <FaGithub className='cursor-pointer inline-block mx-2' size={20}/>
                        </a>
                        <a href='https://www.linkedin.com/in/krisztian-j/' target='_blank'>
                            <FaLinkedinIn className='cursor-pointer inline-block mx-2' size={20}/>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Main;
