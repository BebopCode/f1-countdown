<script setup>
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
 <nav class="w-full p-4">
  <ul class="flex justify-center">
    <li class="mx-5">
      <a class="text-blue-500 hover:text-blue-800" href="/">Active</a>
    </li>
    <li class="mx-5">
      <a class="text-blue-500 hover:text-blue-800" href="/race_countdown">Link</a>
    </li>
    <li class="mx-5">
      <a class="text-blue-500 hover:text-blue-800" href="#">Link</a>
    </li>
  </ul>
</nav>
  <!--<nav class="reusable-div reusable-text">
    <div class="container mx-auto flex justify-center">
      <div>
        <router-link to="/" class="mx-2 hover:text-gray-400">Home</router-link>|
        <router-link to="/race_countdown" class="mx-2 hover:text-gray-400">Race Countdown</router-link>
      </div>
    </div>
  </nav> -->
  <router-view />
</template>


