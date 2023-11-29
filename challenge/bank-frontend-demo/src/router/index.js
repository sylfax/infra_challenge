import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
// import BankView from '../views/BankView.vue'
// import ClientView from '../views/ClientView.vue'
import MainLayout from '../views/MainLayout.vue'
import ClientOnboarding from "@/components/ClientOnboarding.vue";
import ClientLayout from '../views/ClientLayout.vue'
import LoginView from "../views/LoginView.vue"
Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: import.meta.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/bank',
      name: 'bank',
      component: MainLayout
    },
    {
      path: '/client',
      name: 'client',
      component: ClientLayout
    },
    {
      path: "/onboarding",
      name: "ClientOnboarding",
      component: ClientOnboarding
    },
    {
      path: "/login",
      name: "login",
      component: LoginView
    }
  ]
})

export default router
