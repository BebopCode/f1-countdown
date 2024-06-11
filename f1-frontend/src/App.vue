<script setup>
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <nav class="reusable-div reusable-text">
    <div class="container mx-auto flex justify-center">
      <div>
        <router-link to="/" class="mx-2 hover:text-gray-400">Home</router-link>|
        <router-link to="/race_countdown" class="mx-2 hover:text-gray-400">Race Countdown</router-link>
      </div>
    </div>
  </nav>
  <router-view />
</template>


