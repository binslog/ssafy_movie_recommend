<template>
  <div class="home">

    <div class="title">
      <h3>한 주의 PICK</h3>
      <TrendMovie />
    </div>

    <div class="title">
      <h3>평점 높은 순</h3>
      <AlgoMovie />
    </div>

    <div class="title">
      <h3>명작 추천</h3>
      <TopMovie />
    </div>

  </div>
</template>

<script>
import TrendMovie from '@/components/TrendMovie.vue'
import TopMovie from '@/components/TopMovie.vue'
import AlgoMovie from '@/components/AlgoMovie.vue'

export default {
  name: 'HomeView',
  components: {
    TrendMovie,
    TopMovie,
    AlgoMovie,
  },

  
  created() {
    this.getMovies()
    this.getTrendMovies()
    this.getTopMovies()
    this.getAlgoMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    },
    getTrendMovies() {
      this.$store.dispatch('getTrendMovies')
    },
    getTopMovies() {
      this.$store.dispatch('getTopMovies')
    },
    getAlgoMovies() {
      this.$store.dispatch('getAlgoMovies')
    },
  },
}
</script>

<style>

.home{
  background-color: black;
}

.title{
  text-align: left;
  color: white;
  margin: 10px 0px 0px 60px;
}

</style>