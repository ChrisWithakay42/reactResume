import React, {useState} from "react";
import axios from "axios";
import {useForm} from "../context/FormContext.tsx";

interface FormData {
    name: string;
    phone: string;
    email: string;
    subject: string;
    message: string;
}

export const Contact = () => {
    const initialFormData: FormData = {
        name: '',
        phone: '',
        email: '',
        subject: '',
        message: ''
    };
    const {setFormSubmitted} = useForm();

    const [formData, setFormData] = useState<FormData>(initialFormData);
    const [errors, setErrors] = useState<Partial<FormData>>({}); // State for holding validation errors

    const validateForm = (): boolean => {
        const validationRules: { field: keyof FormData; message: string }[] = [
            {field: 'name', message: 'Name is required'},
            {field: 'phone', message: 'Phone number is required'},
            {field: 'email', message: 'Email address is required'},
            {field: 'subject', message: 'Subject is required'},
            {field: 'message', message: 'Message is required'}
        ];

        const validationErrors: Partial<FormData> = {};

        validationRules.forEach(rule => {
            if (!formData[rule.field]) {
                validationErrors[rule.field] = rule.message;
            }
        });

        setErrors(validationErrors);
        return Object.keys(validationErrors).length === 0;
    };


    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();


        if (!validateForm()) {
            return;
        }

        const apiUrl = import.meta.env.VITE_AWS_API_GATEWAY_URL;

        try {
            console.log('apiUrl:', apiUrl);
            const response = await axios.post(apiUrl, formData, {
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            if (response.status === 200) {
                console.log('Form submitted successfully');
                setFormData(initialFormData);
                setFormSubmitted(true);
                const mainElement = document.getElementById('main');
                if (mainElement) {
                    mainElement.scrollIntoView({behavior: 'smooth'});
                }
            }
        } catch (error) {
            console.error('Error sending email:', error);
        }
    };

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        const {name, value} = event.target;
        setFormData((prevFormData) => ({
            ...prevFormData,
            [name]: value
        }));
    };

    return (
        <div id='contact' className='max-w-[90%] md:max-w-[1040px] m-auto md:pl-4 py-16'>
            <h1 className='text-4xl font-bold text-center text-[#001b5e]'>Contact</h1>
            <form onSubmit={handleSubmit} method='POST'>
                <div className='grid md:grid-cols-2 gap-4 w-full py-2 '>
                    <div className='flex flex-col'>
                        <label className='uppercase text-sm py-2'>Name</label>
                        <input
                            className='border-2 rounded-lg p-3 flex border-gray-300'
                            type='text'
                            name='name'
                            value={formData.name}
                            onChange={handleInputChange}
                        />
                        {errors.name && <span className='text-red-500'>{errors.name}</span>}
                    </div>
                    <div className='flex flex-col'>
                        <label className='uppercase text-sm py-2'>Phone</label>
                        <input
                            className='border-2 rounded-lg p-3 flex border-gray-300'
                            type='text'
                            name='phone'
                            value={formData.phone}
                            onChange={handleInputChange}
                        />
                        {errors.phone && <span className='text-red-500'>{errors.phone}</span>}
                    </div>
                </div>
                <div className='flex flex-col py-2'>
                    <label className='uppercase text-sm py-2'>Email</label>
                    <input
                        className='border-2 rounded-lg p-3 flex border-gray-300'
                        type='email'
                        name='email'
                        value={formData.email}
                        onChange={handleInputChange}
                    />
                    {errors.email && <span className='text-red-500'>{errors.email}</span>}
                </div>
                <div className='flex flex-col py-2'>
                    <label className='uppercase text-sm py-2'>Subject</label>
                    <input
                        className='border-2 rounded-lg p-3 flex border-gray-300'
                        type='text'
                        name='subject'
                        value={formData.subject}
                        onChange={handleInputChange}
                    />
                    {errors.subject && <span className='text-red-500'>{errors.subject}</span>}
                </div>
                <div className='flex flex-col py-2'>
                    <label className='uppercase text-sm py-2'>Message</label>
                    <textarea
                        className='border-2 rounded-lg p-3 flex border-gray-300'
                        rows={10}
                        name='message'
                        value={formData.message}
                        onChange={handleInputChange}
                    />
                    {errors.message && <span className='text-red-500'>{errors.message}</span>}
                </div>
                <button type='submit' className='bg-[#001b5e] text-gray-100 mt-1 w-full p-4 rounded-lg'>
                    Submit
                </button>
            </form>
        </div>
    );
};
