<template>

  <div>
    {{ trendmovies }}
  </div>
</template>

<script>
export default {
  name: 'TrendMovie',
  computed: {
    trendmovies() {
      // console.log(this.$store.state.movies)
      return this.$store.state.trends
    },
  },
}
</script>

<style></style>
