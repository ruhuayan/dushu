import { createStore } from 'vuex';
import { Http } from '../models/http-common';

export default createStore({
    state: {
        loading: false,
        books: [],
        chapters: [],
    },
    getters: {
        books: (state) => state.books,

        chapters: (state) => state.chapters,

        // 10 most downloaded books
        mostDownloadedBooks: (state) => {
            const books = [...state.books].sort((a, b) => b.download_ebook_count - a.download_ebook_count)
            return books.slice(0, 9);
        },

        getBookById: (state) => (id) => {
            return state.books.find(book => book.id == id);
        },

        getBookByCategory: (state) => (category) => {
            return state.books.filter(book => book.category == category)
        },

        getBooksByAuthor: (state) => (author) => {
            return state.books.filter(book => book.author == author)
        },
    },
    mutations: {
        SAVE_BOOKS(state, payload) {
            state.books = payload.books;
        },
        SET_LOADING(state, loading) {
            state.loading = loading;
        },
        SAVE_CHAPTERS(state, payload) {
            state.chapters = payload.chapters;
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
        },

        async loadChapters({ state, commit }, payload) {
            if (!state.loading) {
                commit('SET_LOADING', true);

                const res = await Http.get(`books/${payload}/read`);

                commit('SAVE_CHAPTERS', res.data);
                commit('SET_LOADING', false);
            }
        }
    }
})
