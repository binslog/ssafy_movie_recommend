<template>
<div>  
  <div class="container">
    <div class="row row-cols-4">
      <ArticleListItem
        v-for="article in articles"
        :key="article.id"
        :article="article"
      />
  </div>
</div>
</div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  }
}
</script>

<style>
.article-list {
  text-align: start;
}
</style>
