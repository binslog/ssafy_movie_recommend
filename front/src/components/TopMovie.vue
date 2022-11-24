<template>
  <div class="container">
    <div class="row row-cols-5">
      <TopMovieitem
        v-for="(movie, index, movie_id) in topmovies"
        :key="index"
        :movie="movie"
        :movie_id="movie_id"
      />
      <!-- <TestView /> -->
    </div>
  </div>
</template>

<script>
import TopMovieitem from './TopMovieitem.vue'
export default {
  name: 'TopMovie',
  components: {
    TopMovieitem,
  },
  computed: {
    topmovies() {
      // console.log(this.$store.state.movies)
      return this.$store.state.tops
    },
  },
}
</script>

<style></style>
