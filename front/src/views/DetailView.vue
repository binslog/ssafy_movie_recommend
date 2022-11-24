<template>
  <div>
    <!-- <div class="d-flex justify-content-center mb-3 mt-3"> -->
      <div class="wrap" id="test7">
        <b-card no-body  style="width: 500px;">
        
        <div class="login_id">  
          <h3>{{ article?.id }}번째 글</h3>
        </div>

        <hr>        
        <div class="login_id">
          {{ article?.title }}
        </div>
        
        <hr>
        <div class="login_id">
          내용 : {{ article?.title }}
        </div>

        <div class="login_id">
          <p v-if="isCommentszero">
            댓글을 입력해 주세요
          </p>
        </div>

        <div class="login_id">
          <div>
            <p>여기는 댓글 목록입니다.</p>
            <ul
              v-for="(comment, idx) in article.comment_set"
              :key="idx"
              :comment="comment"
            >
            <li>
              {{ comment.content }}
            </li>
            </ul>
          </div>
        </div>

        <router-link
          :to="{ name: 'CommentCreateView', params: { id: article.id } }"
        >
          댓글쓰기
        </router-link>

      </b-card>
    </div>
  <!-- </div> -->
</div>
</template>

<script>
import axios from 'axios'
// import CommentList from '@/components/CommentList'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  data() {
    return {
      comments: {
        // id: {},
      },
      article: {
        id: {},
      },
    }
  },
  components: {
    // List,
  },
  created() {
    // this.getCommentList()
    this.getArticleDetail()
  },
  computed: {
    // comments = this.$store.state
  },
  methods: {
    isCommentszero() {
      if (!this.comments) {
        return true
      }
    },

    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/articles/${this.$route.params.id}/`,
      })

        .then((res) => {

          this.article = res.data
          console.log(this.article)

        })

        .catch((err) => {
          console.log(err)
        })

    },
  },
}
</script>

<style>

#test7 {
   font-family: 'Humanbumsuk';
   color: black;
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
  color:black;
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