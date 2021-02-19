import { createStore } from 'vuex';
import { Http } from '../http-common';

export default createStore({
    state: {
        loading: false,
        books: []
    },
    getters: {
        books: (state) => state.books,

        // 10 most downloaded books
        mostDownloadedBooks: (state) => {
            const books = [...state.books].sort((a, b) => a.download_ebook_count - b.download_ebook_count)
            return books.slice(0, 9);
        },

        getBookById: (state) => (id) => {
            return state.books.find(book => book.id == id);
        },

        getBookByCategory: (state) => (category) => {
            return state.books.filter(book => book.category == category)
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

                const res = await Http.get('books');

                commit('SAVE_BOOKS', res.data);
                commit('SET_LOADING', false);

            }
        }
    }
})
