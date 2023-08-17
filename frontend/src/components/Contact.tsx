import React, {useState} from "react";
import axios from "axios";
import config from "../config.ts"

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

    const [formData, setFormData] = useState<FormData>(initialFormData);
    const [errors, setErrors] = useState<Partial<FormData>>({}); // State for holding validation errors

    const validateForm = (): boolean => {
        const validationErrors: Partial<FormData> = {};

        if (!formData.name) {
            validationErrors.name = 'Name is required';
        }

        if (!formData.phone) {
            validationErrors.phone = 'Phone number is required';
        }

        if (!formData.email) {
            validationErrors.phone = 'Email address is required';
        }

        if (!formData.subject) {
            validationErrors.subject = 'Subject is required';
        }

        if (!formData.message) {
            validationErrors.message = 'Message is required'
        }

        setErrors(validationErrors);
        return Object.keys(validationErrors).length === 0;
    };

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        if (!validateForm()) {
            return;
        }

        try {
            await axios.post(config.apiUrl, formData);
            // Reset the form after successful submission
            setFormData({
                name: '',
                phone: '',
                email: '',
                subject: '',
                message: ''
            });
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
