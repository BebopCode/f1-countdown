import { createWebHistory, createRouter } from "vue-router";
import Home from "../views/Home.vue";
import RaceCountdown from "../views/RaceCountdown.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/race_countdown",
    name: "RaceCountdown",
    component: RaceCountdown,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL), // Use process.env.BASE_URL
  routes,
});

export default router;