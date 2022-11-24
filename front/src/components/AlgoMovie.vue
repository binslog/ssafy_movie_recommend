<template>
  <div class="container">
    <div class="row row-cols-5">
      <AlgoMovieItem
        v-for="(movie, index, movie_id) in algomovies"
        :key="index"
        :movie="movie"
        :movie_id="movie_id"
      />
      <!-- <TestView /> -->
    </div>
  </div>
</template>

<script>
import AlgoMovieItem from './AlgoMovieItem.vue'
export default {
  name: 'TrendMovie',
  components: {
    AlgoMovieItem,
  },
  computed: {
    algomovies() {
      // console.log(this.$store.state.movies)
      return this.$store.state.algos
    },
  },
}
</script>

<style></style>
