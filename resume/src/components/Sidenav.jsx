import React {useState}from "react";
import {AiOutlineMenu} from "react-icons/ai";

const Sidenav = () => {
    const [nav, setNav] = useState(false)
    const handleNav = () => {
        setNav(!nav);
        console.log('state changed')
    };

    return (
       <div>
           <AiOutlineMenu onClick={handleNav}='absolute top-4 z-[99] md:hidden'/>
       </div>
    )
}

export default Sidenav