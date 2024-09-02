<template>
  <div class>
    <div class="reusable-div">
      <img src="@/assets/flag.svg" class="w-1/12 mx-auto" alt="Icon description">
      <h1 class="text-4xl reusable-text">Upcoming: {{ raceTitle }}</h1>
      <h1 class="text-2xl reusable-text">{{ raceLocation }}</h1>
    </div>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else class="w-full p-2 flex flex-col sm:flex-row">
      <div class="sm:w-1/2 w-full p-2">
        <img src="@/assets/car.svg" class="lg:w-1/4 md:w-1/2 sm:w-5/6 mx-auto" alt="Icon description">
        <Countdown :endTime="raceTime" :title="raceText" />
        <Countdown :endTime="qualifyingTime" :title="qualifyingText" />
        <Countdown v-if="isSprintRace" :endTime="sprintTime" :title="sprintText" />
        <Countdown v-if="isSprintRace" :endTime="sprintshootoutTime" :title="sprintShootoutText" />
      </div>
      <div class="sm:w-1/2 w-full p-2">
        <LeaderBoardTable :leaderboardData="leaderboardData" />
        <TeamLeaderBoard :teamLeaderboardData="teamLeaderboardData"/>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Countdown from './Countdown.vue';
import LeaderBoardTable from './LeaderBoardTable.vue';
import TeamLeaderBoard from './TeamLeaderBoard.vue';

export default {
  components: {
    Countdown,
    LeaderBoardTable,
    TeamLeaderBoard
  },
  data() {
    return {
      raceTitle: 'Loading....',
      raceLocation: '',
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
      sprintShootoutText: 'Sprint Shootout Countdown',
      leaderboardData: [],
      teamLeaderboardData: []
    };
  },
  methods: {
    fetchRaceData() {
      axios.get(import.meta.env.VITE_RACE_DATA_URL)
        .then(response => {
          const responseData = response.data[0];
          this.raceTitle = responseData.title;
          this.raceLocation = responseData.location;
          this.raceTime = new Date(responseData.race);
          this.qualifyingTime = new Date(responseData.qualifying);

          if (responseData.sprint !== '') {
            this.isSprintRace = true;
            this.sprintTime = new Date(response.sprint);
            this.sprintShootoutTime = new Date(response.sprint_shootout);
          }
        })
        .catch(error => {
          this.error = 'Failed to load race data: ' + error.message;
        });
    },
    fetchLeaderBoardData() {
      axios.get(import.meta.env.VITE_LEADERBOARD_DATA_URL)
        .then(response => {
          this.leaderboardData = response.data;
        })
        .catch(error => {
          this.error = 'Failed to load leaderboard data: ' + error.message;
        });
    },
    fetchTeamLeaderBoardData() {
      axios.get(import.meta.env.VITE_TEAM_LEADERBOARD_DATA_URL)
        .then(response => {
          this.teamLeaderboardData = response.data;
        })
        .catch(error => {
          this.error = 'Failed to load  team leaderboard data: ' + error.message;
        });
    }
  },
  created() {
    this.loading = true;
    Promise.all([this.fetchRaceData(), this.fetchLeaderBoardData(),this.fetchTeamLeaderBoardData()])
      .finally(() => {
        this.loading = false;
      });
  },
};
</script>