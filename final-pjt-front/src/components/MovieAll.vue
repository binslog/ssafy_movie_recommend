<template>
  <div>
    <!-- movie detail -->
    <!-- {{ movies }} -->
    <MovieAllItem
    v-for="(movie, movie_id) in movies"
    :key="movie_id"
    :movie="movie"
    />
  </div>
</template>

<script>
import MovieAllItem from './MovieAllItem.vue';
export default {
  name: 'MovieAll',
  computed: {
    movies() {
      // console.log(this.$store.state.movies)
      return this.$store.state.movies
    },
  },
  components: {
    MovieAllItem,
  }
}
</script>

<style></style>
