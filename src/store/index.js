import { createStore } from 'vuex';
import { Http } from '../models/http-common';

export default createStore({
    state: {
        loading: false,
        bookLoading: false,
        books: [],
        book: {
            id: null,
            chapters: [],
            series: [],
        }
    },
    getters: {
        books: (state) => state.books,

        book: (state) => state.book,

        mostDownloadedBooks: (state) => (page = 1, perPage = 10) => {
            const books = [...state.books].sort((a, b) => b.download_ebook_count - a.download_ebook_count)
            return {
                total: books.length,
                selected: books.slice(perPage * (page - 1), perPage * page)
            };
        },

        getBookIntroById: (state) => (id) => {
            return state.books.find(book => book.id == id);
        },

        getBooksByCategory: (state) => (category, page = 1, perPage = 10) => {
            const books = state.books.filter(book => book.category == category);
            return {
                total: books.length,
                selected: books.slice(perPage * (page - 1), perPage * page)
            }
        },

        getBooksByAuthor: (state) => (author, page = 1, perPage = 10) => {
            const books = state.books.filter(book => book.author == author)
            return {
                total: books.length,
                selected: books.slice(perPage * (page - 1), perPage * page)
            }
        },

        getBooksByLetter: (state) => (letter = 'A') => {
            return state.books.filter(book => book.alphabet == letter)
        },

        getBooksByQuery: (state) => (query, qtype = 'title', page = 1, perPage = 10) => {
            const regex = new RegExp(query, "gi");
            const books = state.books.filter(book => regex.test(book[qtype])).sort(
                (a, b) => b.download_ebook_count - a.download_ebook_count
            );
            return {
                total: books.length,
                selected: books.slice(perPage * (page - 1), perPage * page)
            }
        },
    },
    mutations: {
        SAVE_BOOKS(state, payload) {
            state.books = payload.books;
        },
        SET_LOADING(state, loading) {
            state.loading = loading;
        },
        SET_BOOK_LOADING(state, loading) {
            state.bookLoading = loading;
        },
        SAVE_BOOK(state, payload, bookId) {
            const book = {
                id: bookId,
                series: payload.series ? payload.series : [],
                chapters: payload.chapters ? payload.chapters : []
            }
            state.book = book;
        },
        UPDATE_BOOK(state, payload) {
            let book = state.books.find(book => book.id == payload.id);
            Object.assign(book, payload);
        }
    },
    actions: {
        async loadBooks({ state, commit }) {
            if (!state.loading) {
                commit('SET_LOADING', true);

                const res = await Http.get('books.php');

                commit('SAVE_BOOKS', res.data);
                commit('SET_LOADING', false);
            }
        },

        async loadChapters({ state, commit }, payload) {
            if (!state.bookLoading) {
                commit('SET_BOOK_LOADING', true);

                const res = await Http.get(`books.php?id=${payload}`);

                commit('SAVE_BOOK', res.data, payload);
                commit('SET_BOOK_LOADING', false);
            }
        },
        async downloadEbook({ commit }, payload) {
            const res = await Http.get(`books.php?id=${payload}&action=ebook-download`);
            commit('UPDATE_BOOK', res.data)
        },
        async downloadPdf({ commit }, payload) {
            const res = await Http.get(`books.php?id=${payload}&action=pdf-download`);
            commit('UPDATE_BOOK', res.data)
        },
        searchBook(_, payload) {
            Http.get(`q?book=${payload}`);
        }
    }
})
