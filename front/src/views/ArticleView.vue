<template>
  <div>
    <div class="title">
      <h3>게시글 목록</h3>

      <div class="button">
        <b-button @click="getdetail" variant="danger">게시글 작성</b-button>
      </div>
    </div>

    <ArticleList />
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList'

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      if (this.isLogin === true) {
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LogInView' })
      }
    },

    getdetail() {
      this.$router.push({ name: 'CreateView' })
    },
  },
}
</script>

<style>
.title {
  text-align: center;
  color: white;
  margin: 10px 0px 0px 60px;
}

.button {
  text-align: right;
  margin: 0px 100px 20px 0px;
}
</style>
