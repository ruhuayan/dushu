import axios from 'axios';

export const Http = axios.create({
    baseURL: `https://dushu.richyan.com/api`,
    // headers: {
    //     Authorization: 'Bearer {token}'
    // }
});