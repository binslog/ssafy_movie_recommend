<template>
  <span class="col d-flex justify-content-center margin mb-4 mt-4">
    <img
      @click="getdetail"
      :src="imageURL"
      class="card-img-top width: 100px margin: 10px"
      alt="사진"
    />
  </span>
</template>

<script>
export default {
  name: 'AlgoMovieItem',
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
