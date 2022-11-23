<template>
  <div class="home" >
    <div class="trend">
      <h4><b>최신 개봉작</b></h4>
    </div>

    <div>
    <TrendMovie />
      최신 개봉작 끝
    </div>


  </div>
</template>

<script>
import TrendMovie from '@/components/TrendMovie.vue'

export default {
  name: 'HomeView',
  components: {
    TrendMovie,
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


<style>

.home{
  background-color: black;
}

.trend{
  text-align: left;
  color: white;
  margin: 10px 0px 0px 60px;
}

</style>