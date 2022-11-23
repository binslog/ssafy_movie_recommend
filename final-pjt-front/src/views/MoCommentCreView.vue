<!-- views/CreateView.vue -->
<!-- 
<template>
  <div>
    <h1>영화평 작성!</h1>
    <form @submit.prevent="createComment">
      <label for="content">내용 :</label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea>
      <br />

      <input type="submit" id="submit" />
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MoCommentCreView',
  data() {
    return {
      movie_id: this.$route.params.id,
      content: null,
      // thismovie : null    ### null 로 기본 설정하면 오류
      // thismovie: 0,
    }
  },
  methods: {
    createComment() {
      const content = this.content

      if (!content) {
        alert('내용을 입력해주세요')
        return
        //AJAX요청을 보내지 않도록 return 시켜 함수 종료
      }
      axios({
        method: 'post',
        url: `${API_URL}/${this.movie_id}/comments/create/`,
        //위의 코드는 장고의 url문법을 따라야 하기에 마지막에 '/'를 붙인다.
        // :id가 맞는가?
        // article_id로 variable routing
        data: {
          content: content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)

          this.$router.push({ name: 'MoviedetailView' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style></style> -->
