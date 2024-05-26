<!-- Countdown.vue -->
<template>
    <div>
      <p>{{ countdown }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      endTime: {
        type: Date,
        required: true
      }
    },
    data() {
      return {
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
        if (diff > 0) {
          const days = Math.floor(diff / (24 * 1000 * 60 * 60));
          const hours = Math.floor((diff % (24 * 1000 * 60 * 60))/(1000 * 60 * 60));
          const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
          const seconds = Math.floor((diff % (1000 * 60)) / 1000);
          this.countdown = `${days}:${hours}:${minutes}:${seconds}`;
        } else {
          this.countdown = 'Countdown expired';
          clearInterval(this.interval);
        }
      }
    }
  };
  </script>
  