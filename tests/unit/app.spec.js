import { mount } from '@vue/test-utils'
import App from "@/App.vue";
import Narbar from '@/components/Narbar.vue';
import Footer from '@/components/Footer';
import { router } from '@/router';
import { store } from '@/store';
// import { nextTick } from 'vue';
// import { createStore } from 'vuex';

describe('App.vue', () => {

    let wrapper;
    beforeEach(() => {
        const expectedData = [1, 2]
        const axios = {
            // create: () => axios,
            get: async () => ({
                data: { expectedData }
            })
        };
        // const $store = {
        //     state: {
        //         loading: false,
        //         books: []
        //     },
        //     commit: jest.fn()
        // }
        wrapper = mount(App, {
            global: {
                plugins: [router, store],
                mocks: {
                    axios
                }
            }
        });
    });

    test('renders App Vue', async () => {

        // test Navbar vue
        expect(wrapper.getComponent(Narbar)).toBeTruthy();

        // test Footer Vue
        expect(wrapper.getComponent(Footer)).toBeTruthy();

        expect(wrapper.find('div.container').classes()).toContain('loading');

        expect(wrapper.find('nav.navbar').classes()).not.toContain('scrolled');

        // expect(store.commit).toHaveBeenCalled()

        // await nextTick()
        // expect(wrapper.find('div.container').classes()).not.toContain('loading');

        // document.documentElement.scrollTop = 15;
        // expect(wrapper.find('nav.navbar').classes()).toContain('scrolled');
    })
})