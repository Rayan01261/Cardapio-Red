// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import TestPage from '@/components/test_page.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: TestPage,
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
