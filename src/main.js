import { createApp } from 'vue';
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import { Categories } from './models/categories';

import 'bootstrap/dist/css/bootstrap.css'

var app = createApp(App);

app.provide('Categories', Categories);

app.use(store)
    .use(router)
    .mount('#app');