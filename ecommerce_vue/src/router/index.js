import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Product from '../views/Product.vue'
import Category from '../views/Category.vue'
import Search from '../views/Search.vue'
import Cart from '../views/Cart.vue'
import SignUp from '../views/SignUp.vue'
import Login from '../views/Login.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/sign-up',
    name: "SignUp",
    component: SignUp
  },
  {
    path: '/log-in',
    name: "Login",
    component: Login
  },
  {
    path: '/search',
    name: "Search",
    component: Search
  },
  {
    path: '/cart',
    name: "Cart",
    component: Cart
  },
  {
    path: '/:category_slug/:product_slug',
    name: "Product",
    component: Product
  },

  {
    path: '/:category_slug',
    name: "Category",
    component: Category
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
