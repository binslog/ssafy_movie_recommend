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
        <div class="wrap" id="test2">
          <div class="login">
            <form @submit.prevent="logIn">
              <h2>Login</h2>

              <div class="login_id">
                <b>ID</b>
                <label for="username"></label>
                <input
                  type="text"
                  id="username"
                  v-model="username"
                  placeholder="ID를 입력하세요."
                />
              </div>

              <div class="login_pw">
                <b>password</b>
                <input
                  type="password"
                  id="password"
                  v-model="password"
                  placeholder="Password를 입력하세요."
                />
              </div>

              <div class="submit">
                <input type="submit" value="submit" />
              </div>
            </form>
          </div>
        </div>
      </body>
    </html>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password
      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    },
  },
  // 만약 로그인이 성공한다면 메인페이지로, 아니라면 alert
}
</script>

<style>
#test2 {
  font-family: 'Humanbumsuk';
}
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
}

a {
  text-decoration: none;
  color: black;
}

li {
  list-style: none;
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

h2 {
  color: tomato;
  font-size: 2em;
}
.login_sns {
  padding: 20px;
  display: flex;
}

.login_sns li {
  padding: 0px 15px;
}

.login_sns a {
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px;
  border-radius: 50px;
  background: white;
  font-size: 20px;
  box-shadow: 3px 3px 3px rgba(0, 0, 0, 0.4), -3px -3px 5px rgba(0, 0, 0, 0.1);
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

.login_etc {
  padding: 10px;
  width: 80%;
  font-size: 14px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: bold;
  color: white;
}

.submit {
  margin-top: 50px;
  width: 80%;
}
.submit input {
  width: 100%;
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
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2210-2@1.0/Humanbumsuk.woff2')
    format('woff2');
  font-weight: normal;
  font-style: normal;
}
</style>
