<template>
    <div>
      moviedetail
      {{ movie }}

    </div>
  </template>
  
  <script>
  export default {
    name: 'MovieDetail',
    computed: {
    //   movies() {
    //     // console.log(this.$store.state.movies)
    //     return this.$store.state.movies
    //   },
    },
    props: {
      movie: Object
    }
  }
  </script>
  
  <style></style>
  