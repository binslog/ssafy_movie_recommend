<template>
  <div id="app">
    <nav class="navbar navbar-expand-sm navbar-dark bg-dark">
      <div class="container-fluid">
      </div>
      <div class="container-fluid">
        <router-link to="/" class="navbar-brand">
          <img alt="Vue logo" src="./assets/logo.png" style="height: 50px;" />
        </router-link>
        <ul class="navbar-nav">
          <li v-if="isLogin !== null" class="nav-item" @click="Logout">
            <router-link :to="{ name: 'home' }" class="nav-link">
              Logout
            </router-link>
          </li>
          <li v-if="isLogin === null" class="nav-item">
            <router-link :to="{ name: 'LogInView' }" class="nav-link">
              Login
            </router-link>
          </li>
          <li v-if="isLogin === null" class="nav-item">
            <router-link :to="{ name: 'SignupView' }" class="nav-link">
              Signup
            </router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{ name: 'articles' }" class="nav-link">
              Community
            </router-link>
          </li>
        </ul>
      </div>
    </nav>
    <router-view />
  </div>
</template>



<script>
export default {
  name: 'App',

  computed: {
    isLogin() {
      console.log(this.$store.state.token)
      return this.$store.state.token
    },
  },
  methods: {
    Logout() {
      console.log('ook')
      this.$store.dispatch('logOut')
      console.log(this.isLogin)
    },
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
