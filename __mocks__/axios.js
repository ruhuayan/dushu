export const axios = {
    create: () => axios,
    get: () => new Promise(res => res({ books: [{ id: 123, }, { id: 124 }] })),
}