import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

import Home from './components/Home.vue'
import Login from './components/Login.vue'

import store from './store' 

const requireAuth = () => (from, to, next) => {
    const isAuthenticated = store.getters.getIsAuth
    if (isAuthenticated) return next()
    next('/login?returnPath=/')
}


export default new VueRouter({
    routes: [
        {
            path: "/",
            name: "Home",
            component: Home,
            beforeEnter: requireAuth()
        },
        {
            path: "/login",
            name: "Login",
            component: Login
        }
    ]
})
