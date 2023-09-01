import Sidenav from "./components/Sidenav";
import Main from "./components/Main";
import Work from "./components/Work.tsx";
import Profile from "./components/Profile.tsx";
import Projects from "./components/Projects.tsx";
import {Contact} from "./components/Contact.tsx";
import {Helmet} from "react-helmet"
import {FormProvider} from "./context/FormContext.tsx";


function App() {

    return (
        <div>
            <Helmet>
                <title>Code With a K</title>
                <meta name={'description'} content={'Python web development consultancy'}/>
            </Helmet>
            <Sidenav/>
            <FormProvider>
                <Main/>
                <Profile/>
                <Work/>
                <Projects/>
                <Contact/>
            </FormProvider>
        </div>
    )
}

export default App