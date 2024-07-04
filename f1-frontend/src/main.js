import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router' // <---
import "@fontsource/quicksand"; // Defaults to weight 400
import "@fontsource/quicksand/400.css"; // Weight 400
import "@fontsource/quicksand/700.css"; // Weight 700 (if you need bold)
createApp(App).use(router).mount('#app')