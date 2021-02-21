import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/about/:category',
        name: 'About',
        props: true,
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    },
    {
        path: '/book/:id',
        name: 'Book',
        props: true,
        component: () => import('../views/Book.vue')
    },
    {
        path: '/author/:name',
        name: 'Author',
        props: true,
        component: () => import('../views/Author.vue')
    },
    {
        path: '/pinyin/:letter',
        name: 'Pinyin',
        props: true,
        component: () => import('../views/Pinyin.vue')
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
