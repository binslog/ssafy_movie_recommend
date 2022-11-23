<template>
  <div class="container">
    <div class="row row-cols-5">
      <MovieAllItem
        v-for="(movie, index, movie_id) in movies"
        :key="index"
        :movie="movie"
        :movie_id="movie_id"
      />
      <!-- <TestView /> -->
    </div>
  </div>
</template>

<script>
import MovieAllItem from './MovieAllItem.vue'
export default {
  name: 'MovieAll',

  computed: {
    movies() {
      // console.log(this.$store.state.movies)
      return this.$store.state.movies
    },

    // onmovie() {
    //   return this.$store.state.movie
    // }
  },
  components: {
    MovieAllItem,
  },
}
</script>

<style></style>
