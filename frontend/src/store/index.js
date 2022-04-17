/* eslint-disable */
import Vue from 'vue';
import Vuex from 'vuex';
import { loginUser, logoutUser, registerUser } from '../services/api/auth';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: null,
    isLoggedIn: false,
  },
  mutations: {
    registerSuccess(state){
      state.user = null;
      state.isLoggedIn = false;
    },
    loginSuccess(state, userId) {
      state.user = userId;
      state.isLoggedIn = true;
    },
    logout(state) {
      state.user = null;
      state.isLoggedIn = false;
    },
  },
  actions: {
    // username, password, password2, firstName, lastName, email
    register({ commit }, {username, password, password2, firstName, lastName, email}){
      return registerUser(username, password, password2, firstName, lastName, email)
        .then (() =>{
          commit({ type: 'registerSuccess', username});
          return Promise.resolve()
        }).catch((err) => {
          commit({type: 'logout'})
          console.log('Register error: ', err)
          return Promise.reject(err);
        })
    },
    login({ commit }, { username, password }) {
      console.log(username, password)
      return loginUser(username, password)
          .then(() => {
          commit({ type: 'loginSuccess', username });
          return Promise.resolve();
        }).catch((error) => {
          commit({ type: 'logout' });
          return Promise.reject(error);
        });
    },
    logout({ commit }) {
      logoutUser();
      commit('logout');
    },
  },
  modules: {
  },
});
