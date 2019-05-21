<template>
  <div>
    <h2>Home</h2>
    <div>{{greeting}}</div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      greeting: ''
    }
  },
  created() {
    axios.get('http://localhost:5000/')  //store.js의 common header에 token을 넣음
      .then(result => this.greeting = result.data)
  }
}
</script><Paste>
