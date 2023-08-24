import {TypeAnimation} from 'react-type-animation'
import {FaGithub, FaLinkedinIn} from "react-icons/fa";
import main from "../assets/main.jpg"
import {useForm} from "../context/FormContext.tsx";
import {useEffect} from "react";
import React from 'react';

const Main = () => {
    const {formSubmitted} = useForm();

    useEffect(() => {
        // Redirect after showing thank you message
        if (formSubmitted) {
            setTimeout(() => {
                window.location.href = '/'; // Redirect to root after a delay
            }, 16000); // Adjust the delay as needed
        }
    }, [formSubmitted]);

    return (
        <div id='main' className='relative h-screen'>
            <img
                className='absolute w-full h-full object-cover object-left scale-x-[-1]'
                src={main}
                alt='Background-image'
            />
            <div className='absolute inset-0 flex justify-center items-center bg-white bg-opacity-50'>
                <div className='p-6 text-center rounded-lg'>
                    {formSubmitted ? (
                        <h2 className='text-2xl pt-4 text-gray-800'>
                            <TypeAnimation
                                sequence={[
                                    'Thank you for reaching out.',
                                    2000,
                                    'I will get back to you ASAP.',
                                    2000,
                                    'Bye.',
                                    2000
                                ]}
                                wrapper='div'
                                cursor={true}
                                repeat={Infinity}
                                speed={50}
                                style={{fontSize: '1em', paddingLeft: '5px'}}
                            />
                        </h2>
                    ) : (
                        <React.Fragment>
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
                                    wrapper='div'
                                    cursor={true}
                                    repeat={Infinity}
                                    speed={50}
                                    style={{fontSize: '1em', paddingLeft: '5px'}}
                                />
                            </h2>
                        </React.Fragment>
                    )}
                    <div className='pt-6'>
                        <FaGithub
                            className='cursor-pointer inline-block mx-2'
                            size={20}
                            onClick={() => window.open('https://github.com/ChrisWithakay42', '_blank')}
                        />
                        <FaLinkedinIn
                            className='cursor-pointer inline-block mx-2'
                            size={20}
                            onClick={() => window.open('https://www.linkedin.com/in/krisztian-j/', '_blank')}
                        />
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Main;
