import { createStore } from 'vuex';
import { Http } from '../http-common';

export default createStore({
    state: {
        loading: false,
        books: []
    },
    getters: {
        get: (state) => state,

        getBookById: (state) => (id) => {
            return state.books.find(book => book.id === id)
        }
    },
    mutations: {
        SAVE_BOOKS(state, payload) {
            state.books = payload.books;
        },
        SET_LOADING(state, loading) {
            state.loading = loading
        }
    },
    actions: {
        async loadBooks({ state, commit }) {
            if (!state.loading) {
                commit('SET_LOADING', true);

                const res = await Http.get('most_downloaded_books');

                commit('SAVE_BOOKS', res.data);
                commit('SET_LOADING', false);

            }
        }
    }
})
