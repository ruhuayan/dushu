import { createSSRApp } from 'vue';
import App from './App.vue'
import router from './router'
import store from './store'

import 'bootstrap/dist/css/bootstrap.css'
import titleMixin from './mixins/titleMixin';

export const createApp = () => {
    const app = createSSRApp(App)
        .use(store)
        .use(router)
        .mixin(titleMixin);
    return { app, router }
}