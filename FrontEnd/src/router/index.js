// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import TestPage from '@/components/Home.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: TestPage,
  },
  {
    path: '/mesas',
    name: 'mesas',
    component: () => import('@/components/Mesas.vue'),
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
