import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'
import { registerLicense } from '@syncfusion/ej2-base';

const syncFusionLicense = import.meta.env.VITE_SYNCFUSION_LICENSE_KEY
// registerLicense('Ngo9BigBOggjHTQxAR8/V1NGaF1cXGNCd0x0Rnxbf1xzZFZMY1VbRnRPIiBoS35RdUVrW3tfdXBcQ2ZbUEVy');
registerLicense(syncFusionLicense)
ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
