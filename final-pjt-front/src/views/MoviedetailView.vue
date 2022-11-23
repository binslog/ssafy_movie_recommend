<template>
<div>  
  <div>
    <div class="d-flex justify-content-center mb-3 mt-3">
      <b-card no-body class="overflow-hidden" style="max-width: 750px;">
        <b-row no-gutters>

          <b-col md="6">
            <b-card-img :src="imageURL" alt="Image" class="movie"></b-card-img>  
          </b-col>

          <b-col md="6">
            <b-card-body :title="thismovie.title">
            <hr>
            
          <div class="test">
                <div class="genres">
                  개봉날짜: {{ thismovie.released_date }}              
                </div>

                <div class="release_date">
                  장르: {{ thismovie.genres }}
                </div>

              <hr>

                <div class="overview">
                  {{ thismovie.overview }}
                </div>

            </div>

            </b-card-body>
          </b-col>

        </b-row>
      </b-card>
    </div>

  <div class="button">
    <b-button @click="getback" variant="danger" >영화 목록</b-button>
  </div>
  </div>
</div>
</template>


<script>
const API_URL = 'http://127.0.0.1:8000'
import axios from 'axios'
export default {
  name: 'MoviedetailView',
  computed: {
    movie() {
      console.log(this.$store.state.movie)
      return this.$store.state.movies
    },

    imageURL() {
      console.log(this.thismovie)
      return `https://image.tmdb.org/t/p/w500${this.thismovie.poster_path}`
    },

    // onmovie() {
    //   return this.$store.state.movie
    // }
  },
  data() {
    return {
      movie_id: this.$route.params.movie_id,
      check: this.$route.params.check,

      // thismovie : null    ### null 로 기본 설정하면 오류가 나더라... 아고 너무 힘들다...ㅠㅠ
      thismovie: 0,
    }
  },

  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/`,
      })
        .then((res) => {
          console.log(res.data)
          this.thismovie = res.data
        })
        .catch((err) => console.log(err))
    },
    getback() {
      this.$router.push({ name: 'home' })
    },
  },


  created() {
    this.getMovieDetail()
  },
}

</script>

<style>

.test {
   font-family: 'Humanbumsuk',sans-serif;;
}

.button {
  align-items: flex-end;
  margin: 0px 10px 0px 0px;
}
</style>
