import Vue from 'vue'
import store from '../store'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Product from '../views/Product.vue'
import Category from '../views/Category.vue'
import Search from '../views/Search.vue'
import Cart from '../views/Cart.vue'
import SignUp from '../views/SignUp.vue'
import Login from '../views/Login.vue'
import MyAccount from '../views/MyAccount.vue'

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
    path: '/my-account',
    name: "MyAccount",
    component: MyAccount,
    meta: {
      requireLogin: true,
    }
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

router.beforeEach((to, from, next) => {

  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({
      name: "Login",
      query: { to: to.path }
    }  )
  }
  else {
    next()
  }
})
export default router
