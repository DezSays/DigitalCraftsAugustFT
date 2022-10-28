import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import ContactManagement from './components/ContactManagement';
import BaseLayout from './layout/BaseLayout';
import 'bootstrap/dist/css/bootstrap.min.css';




const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Router>
      <BaseLayout>
      <Routes>
        <Route path='/' element={<App />} />
        <Route path='/contact' element={<ContactManagement />} />
        
      </Routes>
      </BaseLayout>
    </Router>
  </React.StrictMode>
);

