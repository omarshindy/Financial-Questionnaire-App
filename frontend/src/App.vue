<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" variant="info">
      <router-link to="/" tag="b-navbar-brand">Xpov Task</router-link>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <router-link v-if="!isLoggedIn" to="/register" tag="b-nav-item">Register</router-link>
          <router-link v-if="!isLoggedIn" to="/login" tag="b-nav-item">Login</router-link>
          <b-nav-item v-else v-on:click="handleLogout" tag="b-nav-item">Logout</b-nav-item>
          <router-link to="/questions" tag="b-nav-item">Questionnaire</router-link>
        </b-navbar-nav>
      </b-collapse>

    </b-navbar>
    <router-view/>

  </div>
</template>

<script>
/* eslint-disable */
import { mapActions, mapState } from 'vuex';

export default {
  name: 'App',
  computed: {
    ...mapState(['isLoggedIn']),
  },
  methods: {
    handleLogout(event) {
      event.preventDefault();
      this.logout();
      this.$router.push('/questions');
    },
    ...mapActions(['logout']),
  },
};
</script>

<style>
#app 
{
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav 
{
  padding: 30px;
}

#nav a 
{
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active 
{
  color: #42b983;
}
</style>
