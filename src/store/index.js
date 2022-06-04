import { createStore } from 'vuex';
import { Http } from '../models/http-common';

export const DUSHU = 'dushu';
export const LEN = 10;

export default createStore({
    state: {
        loading: false,
        bookLoading: false,
        books: [],
        book: {
            id: null,
            chapters: [],
            series: [],
            scrollY: 0,
        }
    },
    getters: {
        books: (state) => state.books,

        book: (state) => state.book,

        mostDownloadedBooks: (state) => (page = 1, perPage = 10) => {
            const books = [...state.books].sort((a, b) => b.e_count - a.e_count)
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
                (a, b) => b.e_count - a.e_count
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
        SAVE_BOOK(state, payload) {
            const { id, data, scrollY = null } = payload;
            state.book = { id, ...data, scrollY };
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

                const d = localStorage.getItem(DUSHU);
                let dushu = [];
                const book = { id: payload, scrollY: 0 };
                try {
                    dushu = await JSON.parse(d) ?? [];
                    const idx = dushu.findIndex(book => book.id === payload);
                    if (idx < 0) throw 'Not Found';

                    Object.assign(book, dushu[idx]);
                    dushu.splice(idx, 1);
                    dushu.push(book);
                    localStorage.setItem(DUSHU, JSON.stringify(dushu));
                } catch {
                    const res = await Http.get(`books.php?id=${payload}`);
                    book.data = res.data;
                    if (dushu.length >= LEN) dushu.shift();
                    dushu.push(book);
                    localStorage.setItem(DUSHU, JSON.stringify(dushu));
                }
                commit('SAVE_BOOK', book);
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
        },
        setBookScrollY(_, payload) {
            try {
                const d = localStorage.getItem(DUSHU);
                const dushu = JSON.parse(d) ?? [];
                const book = dushu.find(b => b.id === payload.id);
                if (!book) throw `Book (${payload.id}) not found`;

                Object.assign(book, payload);

                localStorage.setItem(DUSHU, JSON.stringify(dushu));
            } catch(e) {
                console.error(e)
            }
        }
    }
})
