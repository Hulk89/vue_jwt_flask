<template>
  <div>
    <router-link to="/">Home</router-link>
    <a href="" v-if="isAuthenticated" @click.prevent="onClickLogout">Logout</a>
    <router-link to="/login" v-else>Login</router-link>
  </div>
</template>

<script>
  import store from '../store'
  export default {
    computed: {
      isAuthenticated() {
        return store.getters.getIsAuth
      }
    },
    methods: {
      onClickLogout() {
          store.dispatch('LOGOUT').then(() => {
              console.log(this.$router)
              this.$router.go({path: '/',
                               force: true})  //똑같은 페이지일 때도 강제로 refresh
          })
      }
    }
  }
</script>
