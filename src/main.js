import { createApp } from 'vue';
import App from './App.vue'
import router from './router'
import store from './store'

import 'bootstrap/dist/css/bootstrap.css'
import titleMixin from './mixins/titleMixin';

var app = createApp(App);

app.use(store)
    .use(router)
    .mixin(titleMixin)
    .mount('#app');