import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'
import { registerLicense } from '@syncfusion/ej2-base';

const syncFusionLicense = import.meta.env.VITE_SYNCFUSION_LICENSE_KEY
registerLicense(syncFusionLicense)
ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
