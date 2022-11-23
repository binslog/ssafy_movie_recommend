<template>
  <div class="container">
    <div class="row row-cols-5">
      <TrendMovieItem
        v-for="(movie, index, movie_id) in trendmovies"
        :key="index"
        :movie="movie"
        :movie_id="movie_id"
      />
      <!-- <TestView /> -->
    </div>
  </div>
</template>

<script>
import TrendMovieItem from './TrendMovieItem.vue'
export default {
  name: 'TrendMovie',
  components: {
    TrendMovieItem,
  },
  computed: {
    trendmovies() {
      // console.log(this.$store.state.movies)
      return this.$store.state.trends
    },
  },
}
</script>

<style></style>
