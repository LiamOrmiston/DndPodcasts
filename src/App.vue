<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <Rss test="Art of the Roll"/>
  </div>
</template>

<script>
import Rss from './components/Rss.vue'

export default {
  name: 'App',
  components: {
    Rss
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
