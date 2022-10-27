import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './components/App';
import News from './components/News'
import Forms from './components/Forms'
import FormClass from './components/FormClass';
import BaseLayout from './components/layout/BaseLayout';
import ShoppingList from './components/ShoppingList';
import Contacts from './components/Contacts';
import { BrowserRouter as Router, Routes as Switch, Route } from 'react-router-dom'


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Router>
      <BaseLayout>
        <Switch>
          <Route path='/' element={<App />} />
          <Route path='/forms' element={<Forms />} />
          <Route path='/formclass' element={<FormClass />} />
          <Route path='/news' element={<News />} />
          <Route path='/shoppinglist' element={<ShoppingList />} />
          <Route path='/contacts' element={<Contacts />} />
        </Switch>
      </BaseLayout>
    </Router> 
  </React.StrictMode>
);

