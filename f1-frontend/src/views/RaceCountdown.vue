<template>
    <div class="flex-col">
      <h1 class="text-2xl reusable-div reusable-text">{{ raceTitle }}</h1>
      <div v-if="loading">Loading...</div>
      <div v-else-if="error">{{ error }}</div>
      <div v-else class="container w-full p-4">
        <Countdown :endTime="raceTime" :title="raceText" />
        <Countdown :endTime="qualifyingTime" :title="qualifyingText" />
        <Countdown v-if="isSprintRace" :endTime="sprintTime" :title="sprintText"/>
        <Countdown v-if="isSprintRace" :endTime="sprintshootoutTime" :title="sprintShootoutText" />
        
      
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import Countdown from './Countdown.vue';

  export default {
    components: {
    Countdown
    },
    data() {
      return {
        raceTitle: 'asdasd',
        raceTime: null,
        qualifyingTime: null,
        sprintTime: null,
        sprintShootoutTime: null,
        loading: true,
        error: null,
        isSprintRace: false,
        raceText: 'Race Countdown',
        qualifyingText: 'Qualifying Countdown',
        sprintText: 'Sprint Countdown',
        sprintShootoutText: 'Sprint Shootout Countdown'
      };
    },
    methods: {
      fetchRaceData() {
        axios.get('http://127.0.0.1:8000/api/race_data/')
          .then(response => {
            const responseData = response.data[0];
            this.raceTitle = responseData.title;
            this.raceTime = new Date(responseData.race);
            this.qualifyingTime = new Date(responseData.qualifying);
            
            if (responseData.sprint !== null) {
            this.isSprintRace = true;
            this.sprintTime = new Date(response.sprint);
            this.sprintShootoutTime = new Date(response.sprint_shootout);
            }
            
            this.loading = false;
          })
          .catch(error => {
            this.error = 'Failed to load race data: ' + error.message;
            this.loading = false;
          });
      },
    },
    created() {
      this.fetchRaceData();

    },
  };
  </script>