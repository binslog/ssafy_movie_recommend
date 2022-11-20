<template>
    <div>
      <img :src="imageURL" alt="사진">
      <button>Details</button>
    </div>
</template>
  
  <script>
 
  export default {
    name: 'MovieAllItem',
    props: {
        movie: Object,
    },

    computed : {
        imageURL() {
          return `https://image.tmdb.org/t/p/w500${this.movie.poster_path}`
        }
        
    },
 
    
  }
  </script>
  
  <style></style>
  