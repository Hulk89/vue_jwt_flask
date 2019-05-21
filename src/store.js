import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const resourceHost = 'http://localhost:5000'  // flask

export default new Vuex.Store({
  state: {
    accessToken: null
  },
  getters: {
    getIsAuth: function(state) {
      return  state.accessToken
    }
  },
  mutations: {
    LOGIN (state, accessToken) {
      state.accessToken = accessToken
    },
    LOGOUT (state) {
      state.accessToken = null
    }
  },
  actions: {
    LOGIN ({commit}, {id, password}) {
      return axios.post(`${resourceHost}/login`,
                        {user: id, password: password})
        .then( ({data}) => {
            commit('LOGIN', data.token)

            axios.defaults.headers.common['Authorization'] =
                `Bearer ${data.token}`
        })
    },
    LOGOUT ({commit}) {
      axios.defaults.headers.common['Authorization'] = undefined
      commit('LOGOUT')
    },
  }
})
