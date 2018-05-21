import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

import App from './App';
import Layout from './Layout'
import Form from './Form'

import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();

ReactDOM.render(<Layout />, document.getElementById('layout'));
registerServiceWorker();

ReactDOM.render(<Form />, document.getElementById('form'));
registerServiceWorker();
