import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

const API_URL = 'http://127.0.0.1:8000'
// let detail_url = 'http://127.0.0.1:8000/movies/:modvie_id/'
Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    articles: [],
    token: null,
    movies: [],
    trends: [],
    movie: [],
    comments: [],
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
  },
  mutations: {
    // GET_MOVIEDETAIL(state, movie) {
    //   state.movie = movie
    // },
    GET_MOVIES(state, movies) {
      state.movies = movies
      // console.log(state.movies)
    },
    GET_TRENDMOVIES(state, trends) {
      state.trends = trends
      // console.log(state.movies)
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'home' })
    },
    DELETE_TOKEN(state) {
      console.log(state.token)
      state.token = null
      router.push({ name: 'home' })
    },
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
        // headers: {
        //   Authorization: `Token ${context.state.token}`,
        // },
      })
        .then(
          (res) => context.commit('GET_MOVIES', res.data),
          // console.log('성공', context, res),
        )
        .catch((err) => console.log(err))
    },
    // 이걸 무비 디테일에 넣어보자..
    // getMoviedetail(context) {
    //   axios({
    //     method: 'get',
    //     url: detail_url

    //   })
    //     .then(
    //       (res) => context.commit('GET_MOVIEDETAIL', res.data),
    //       console.log('성공', context),
    //     )
    //     .catch((err) => console.log(err))

    getTrendMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/trend/`,
        // headers: {
        //   Authorization: `Token ${context.state.token}`,
        // },
      })
        .then(
          (res) => context.commit('GET_TRENDMOVIES', res.data),
          // console.log('성공', context, res),
        )
        .catch((err) => console.log(err))
    },

    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username,
          password1,
          password2,
        },
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,

        data: {
          username: payload.username,
          password: payload.password,
        },
      })
        .then((res) => {
          console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    logOut(context) {
      console.log('ok"')
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
      })
        .then((res) => {
          console.log(res)
          context.commit('DELETE_TOKEN', res.data.key)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/articles/`,
        headers: {
          Authorization: `Token ${context.state.token}`,
        },
      })
        .then((res) => {
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
})
