
export const Contact = () => {
    return (
        <div id='contact' className='max-w-[90%] md:max-w-[1040px] m-auto md:pl-4 py-16'>
            <h1 className='text-4xl font-bold text-center text-[#001b5e]'>Contact</h1>
            <form action='' method='POST' encType='multipar/form-data'>
                <div className='grid md:grid-cols-2 gap-4 w-full py-2 '>
                    <div className='flex flex-col'>
                        <label className='uppercase text-sm py-2'>Name</label>
                        <input className='border-2 rounded-lg p-3 flex border-gray-300' type='text' name='name'/>
                    </div>
                    <div className='flex flex-col'>
                        <label className='uppercase text-sm py-2'>Phone</label>
                        <input className='border-2 rounded-lg p-3 flex border-gray-300' type='text' name='phone'/>
                    </div>
                </div>
                <div className='flex flex-col py-2'>
                    <label className='uppercase text-sm py-2'>Email</label>
                    <input className='border-2 rounded-lg p-3 flex border-gray-300' type='email' name='email'/>
                </div>
                <div className='flex flex-col py-2'>
                    <label className='uppercase text-sm py-2'>Subject</label>
                    <input className='border-2 rounded-lg p-3 flex border-gray-300' type='text' name='subject'/>
                </div>
                <div className='flex flex-col py-2'>
                    <label className='uppercase text-sm py-2'>Message</label>
                    <textarea  className='border-2 rounded-lg p-3 flex border-gray-300' rows={10} name='message'></textarea>
                </div>
                <button className='bg-[#001b5e] text-gray-100 mt-1 w-full p-4 rounded-lg'>Submit</button>
            </form>
        </div>
    )
}