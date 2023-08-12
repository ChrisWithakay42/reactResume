import Sidenav from "./components/Sidenav";
import Main from "./components/Main";
import Work from "./components/Work.tsx";
import Profile from "./components/Profile.tsx";
import Projects from "./components/Projects.tsx";
import {Contact} from "./components/Contact.tsx";

function App() {

    return (
        <div>
            <Sidenav />
            <Main />
            <Profile/>
            <Work/>
            <Projects />
            <Contact />
        </div>
  )
}

export default App