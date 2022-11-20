<template>

	<nav class="navbar navbar-expand-sm navbar-light bg-light">
		<div class="container-fluid">
			<router-link to="/" class="navbar-brand">
				<img alt="Vue logo" src="./assets/samsung.png" style="height:50px;" />
			</router-link>
			<ul class="navbar-nav">
				<li class="nav-item">
					<router-link :to="{ name: 'login' }" class="nav-link">Login</router-link>
				</li>
				<li class="nav-item">
					<router-link :to="{ name: 'signup' }" class="nav-link">Signup</router-link>
				</li>
				<li class="nav-item">
					<router-link :to="{name: 'community'}" class="nav-link">Community</router-link>
				</li>
			</ul>
		</div>
	</nav>

</template>



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
