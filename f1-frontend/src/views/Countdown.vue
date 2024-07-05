<!-- Countdown.vue -->
<template>
    <div class="reusable-div">
      <h2 class="text-xl md:text-2xl reusable-text">{{ race_text }}</h2>
      <h2 class="md:text-3xl sm:text-2xl text-1xl reusable-text">{{ countdown }}</h2>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      endTime: {
        type: Date,
        required: true
      },
      title:{
        type: String,
        required: true
      }
    },
    data() {
      return {
        race_text:'',
        countdown: ''
      };
    },
    mounted() {
      this.updateCountdown();
      this.interval = setInterval(this.updateCountdown, 1000);
    },
    beforeDestroy() {
      clearInterval(this.interval);
    },
    methods: {
      updateCountdown() {
        const now = new Date();
        const diff = this.endTime - now;
        this.race_text = this.title; 
        if (diff > 0) {
          const days = Math.floor(diff / (24 * 1000 * 60 * 60));
          const hours = Math.floor((diff % (24 * 1000 * 60 * 60))/(1000 * 60 * 60));
          const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
          const seconds = Math.floor((diff % (1000 * 60)) / 1000);
          this.countdown = `${days}D:${hours}H:${minutes}M:${seconds}S`;
        } else {
          this.countdown = 'Countdown expired';
          clearInterval(this.interval);
        }
      }
    }
  };
  </script>
  