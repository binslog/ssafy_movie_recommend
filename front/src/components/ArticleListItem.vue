<template>
  <div>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Document</title>
        <link
          href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap"
          rel="stylesheet"
        />
      </head>

      <body>
        <div class="wrap_list">
          <div class="articlelist">
            <h5>{{ article.id }} 번째 글</h5>
            <p>작성자 : {{ article.username }}</p>
            <p>제목 : {{ article.title }}</p>

            <!-- <router-link :to="{ name: 'DetailView', params: { id: article.id } }"> [자세히 보기] </router-link> -->

            <div class="button_detail">
              <router-link
                :to="{ name: 'DetailView', params: { id: article.id } }"
              >
                [DETAIL]
              </router-link>
            </div>
            <hr />
            <div class="button_delete">
              <b-button @click="getdelete" variant="danger">[지우기]</b-button>
            </div>
          </div>
        </div>
      </body>
    </html>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  },
  data() {
    return {
      article_id: this.article.id,
    }
  },

  methods: {
    // getdetail() {
    //   this.$router.push({ name: 'DetailView' , params: $this.})
    // },

    getdelete() {
      axios({
        method: 'delete',
        url: `${API_URL}/articles/${this.article_id}/`,
      })
        .then((res) => {
          this.$store.dispatch('getArticles')
          console.log(res.data)
          console.log('ok')
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style>
.wrap_list {
  width: 100%;
  height: 30vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: aliceblue;
  font-family: 'Noto Sans KR', sans-serif;
  margin: 20px 0px 5px 10px;
}

.articlelist {
  width: 90%;
  text-align: left;
  color: black;
  margin: 20px 0px 5px 10px;
}
</style>
