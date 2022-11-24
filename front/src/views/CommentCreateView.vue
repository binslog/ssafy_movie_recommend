<!-- views/CreateView.vue -->

<template>
<div>
  <div class="wrap" id="test4">
    <h2>댓글을 작성하세요</h2>

    <form @submit.prevent="createComment">

      <div class="login_id">          
        <textarea id="content" cols="30" rows="10" v-model="content"></textarea>
      </div>
      
      <div class="submit">
      <input type="submit" id="submit" value="댓글 작성" />
      </div>
    </form>
  </div>
</div>  
</template>


<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentCreateView',
  data() {
    return {
      article_id: this.$route.params.id,
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
        url: `${API_URL}/articles/${this.article_id}/comments/`,
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

          this.$router.push({ name: 'DetailView' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style>
#test4 {
   font-family: 'Humanbumsuk';
}

.wrap {
  width: 100%;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.1);
  font-family: 'Noto Sans KR', sans-serif;
}

.login {
  width: 40%;
  height: 600px;
  background: black;
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

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

.submit {
margin-top: 50px;
  width: 80%;
}

.submit input {
  width: 120%;
  height: 50px;
  border: 0;
  outline: none;
  border-radius: 40px;
  background: linear-gradient(to left, rgb(255, 77, 46), rgb(255, 155, 47));
  color: white;
  font-size: 1.2em;
  letter-spacing: 2px;
}


@font-face {
    font-family: 'Humanbumsuk';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2210-2@1.0/Humanbumsuk.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}
</style>
