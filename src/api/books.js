import axios from 'axios';

export const booksApi = axios.create({
    baseURL: `https://jt3xt3j97c.execute-api.us-east-2.amazonaws.com/`
})