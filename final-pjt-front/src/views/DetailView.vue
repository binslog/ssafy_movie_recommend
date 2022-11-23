<template>
  <div>
    <div class="d-flex justify-content-center mb-3 mt-3">
  <b-card no-body class="overflow-hidden" style="max-width: 500px;">
    <h3>{{ article?.id }}번째 글</h3>
    <hr>
    <h3><b> {{ article?.title }} </b></h3>
    <hr>
    <p>내용 : {{ article?.content }}</p>
    
    <hr>
    <p>작성시간 : {{ article?.created_at }}</p>
    <div>
    <hr>
      <p v-if="isCommentszero">
        덧글을 입력해 주세요
      </p>

      <p v-else>
        덧글 목록
        <ul>
          <li
            v-for="(comment, id) in comments"
            :key ="id"
            :comment="comment">
            {{ comment.content }}

          </li>
        </ul>
      </p>
    </div>

    <router-link
      :to="{ name: 'CommentCreateView', params: { id: article.id } }"
    >
      댓글쓰기
    </router-link>

    <p>여기는 덧글 목록입니다.</p>
    
    <!-- <ul>
      <li 
      v-for="(comment, id) in comments"
      :key="id"
      :comment="comment"
      >
    {{ comment.content }} 
    </li>
    </ul> -->
  
  </b-card>
  </div>
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
    // CommentList,
  },
  created() {
    this.getCommentList()
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
    getCommentList() {
      axios({
        method: 'get',
        url: `${API_URL}/articles/comments/`,
      })
        .then((res) => {
          console.log(res.data)
          this.comments = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },

    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/articles/${this.$route.params.id}/`,
        //위에서 에러가 났으니 article_id등으로 시험
        // url: `${API_URL}/articles/${this.$route.params.id}/`가 아닌가..?
      })
        .then((res) => {
          console.log(res)
          this.article = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>
