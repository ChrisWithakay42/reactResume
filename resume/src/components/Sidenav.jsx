import React {useState} from "react";
import {AiOutlineMenu} from "react-icons/ai";

const Sidenav = () => {
    const [nav, setNav] = useState(false)
    const handleNav = () => {
        setNav(!nav);
    };

    return (
        <div>
            <AiOutlineMenu onClick={handleNav}='absolute top-4 z-[99] md:hidden'/>
            {
                nav ? (
                        <div>
                            <a href'#main'>
                                <AiOutlineMenu />
                            </a>

                        </div>
                    )
                    : (
                        <div></div>
                    )
            }
        </div>
    )
}

export default Sidenav