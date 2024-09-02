<script setup>
import HelloWorld from './components/HelloWorld.vue'
</script>

<template >
 <nav class="w-full p-4">
  <ul class="flex justify-center">
    <li class="mx-5">
      <a class="text-slate-500 hover:text-slate-800 selection:underline" href="/">Countdown</a>
    </li>
    <li class="mx-5">
      <a class="text-slate-500 hover:text-slate-800" href="https://www.formula1.com/en/racing/2024">Official Calender</a>
    </li>
    <li class="mx-5">
      <a class="text-slate-500 hover:text-slate-800" href="https://github.com/BebopCode/f1-countdown">Github</a>
    </li>
  </ul>
</nav>
  <router-view />
  <footer class="bg-zinc-50 text-center dark:bg-neutral-700 lg:text-left text-sm">
  <div class="bg-black/5 p-4 text-center  text-white">
    This website is unofficial and is not associated in any way with the Formula 1 companies.

F1, FORMULA ONE, FORMULA 1, FIA FORMULA ONE WORLD CHAMPIONSHIP, GRAND PRIX and related marks are trade marks of Formula One Licensing B.V.
    
  </div>
</footer>
</template>


