import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Createuser from '@/components/Createuser'
import Createticket from '@/components/Createticket'
import Dashboarduser from '@/components/Dashboarduser'
import Dashboard from '@/components/Dashboard'

Vue.use(Router)


export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/createuser',
      name: 'createuser',
      component: Createuser
    },
    {
      path: '/createticket',
      name: 'createticket',
      component: Createticket
    },
    {
      path: '/dashboarduser',
      name: 'dashboarduser',
      component: Dashboarduser
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard
    },
  ]
})
