<!-- views/CreateView.vue -->

<template>
<div class="d-flex justify-content-center mb-3 mt-3">
  <b-card no-body class="overflow-hidden" style="max-width: 500px;">
    <form @submit.prevent="createArticle">.
      <h2>게시글 작성</h2>
      <hr>
      <div class="login_id">
      <label for="title">제목 :</label>
      </div>
      
      <input type="text" id="title" v-model.trim="title" placeholder="제목을 입력하세요." />
      
      <hr>
      <label for="content">내용 :</label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea>
      
      <hr>
      <input type="submit" id="submit" />

    </form>
  </b-card>
</div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CreateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
        //AJAX요청을 보내지 않도록 return 시켜 함수 종료
      }
      axios({
        method: 'post',
        url: `${API_URL}/articles/`,
        //위의 코드는 장고의 url문법을 따라야 하기에 마지막에 '/'를 붙인다.
        data: {
          title: title,
          content: content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          this.$router.push({ name: 'articles' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style>

.login_id {
  width: 90%;
  text-align: left;
  color: white;
  margin: 20px 10px 5px 10px;
}

.login_id input {
  width: 100%;
  height: 50px;
  border-radius: 30px;
  margin-top: 10px;
  padding: 0px 20px;
  border: 1px solid lightgray;
  outline: none;
}

.login_pw {
  margin: 20px 10px 5px 10px;
  text-align: left;
  width: 100%;
  color: white;
}

.login_pw input {
  width: 90%;
  height: 50px;
  border-radius: 30px;
  margin-top: 10px;
  padding: 0px 20px;
  border: 1px solid lightgray;
  outline: none;
}
</style>
