<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />

    <div>homeview입니다.</div>
    <div>
      무비올 시작
      <!-- <MovieAll /> -->
      여기까지 무비올
      <TrendMovie />
    </div>

    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <!-- <SignLogin /> -->
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
// import SignLogin from '../components/SignLogin.vue'

// import NavBar from '@/components/NavBar.vue'
// import MovieAll from '@/components/MovieAll.vue'
import TrendMovie from '@/components/TrendMovie.vue'

export default {
  name: 'HomeView',
  components: {
    // NavBar,
    // MovieAll,
    TrendMovie,

    // HelloWorld,
  },

  created() {
    this.getMovies()
    this.getTrendMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    },
    getTrendMovies() {
      this.$store.dispatch('getTrendMovies')
    },
  },
}
</script>
