<template>
  <div class="container">
    <div class="d-flex justify-content-center">
      "
      <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="4000"
        controls
        indicators
        background="#ababab"
        img-width="500"
        img-height="300"
        style="text-shadow: 1px 1px 2px #333; width: 400px;"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
      >
        <TrendMovieItem
          v-for="(movie, index, movie_id) in trendmovies"
          :key="movie.id"
          :movie="movie"
          :movie_id="movie_id"
        />
      </b-carousel>

      <hr />
      <div></div>
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

    computed: {
      imageURL() {
        return `https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
      },
    },
  },
}
</script>

<style></style>
