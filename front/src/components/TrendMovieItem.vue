<template>
  <div class="box" @click="getdetail">
    <b-carousel-slide :img-src="imageURL"></b-carousel-slide>
  </div>
</template>

<script>
export default {
  name: 'TrendMovieItem',
  props: {
    movie: Object,
    movie_id: Number,
  },

  computed: {
    imageURL() {
      return `https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
    },
  },

  methods: {
    getdetail() {
      // this.$router.push({name : 'detail'})
      this.$router.push({
        name: 'MovieDetail',
        params: { movie_id: this.movie.movie_id, check: '재대로왓나..' },
      })
    },
  },
}
</script>

<style></style>
