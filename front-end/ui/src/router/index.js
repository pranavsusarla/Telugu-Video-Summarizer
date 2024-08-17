import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/components/HomePage.vue'
import SummarizeLocal from '@/components/SummarizeLocal.vue'
import SummarizeYouTube from '@/components/SummarizeYouTube.vue'
import Summary from '@/components/Summary.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/summarizeYouTube',
    name: 'summarizeYouTube',
    component: SummarizeYouTube
  },
  {
    path: '/summarizeLocal',
    name: 'summarizeLocal',
    component: SummarizeLocal
  },
  {
    path: '/summary',
    name: 'Summary',
    component: Summary
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
