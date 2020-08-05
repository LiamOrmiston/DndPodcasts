<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <Rss test="Art of the Roll"/>
  </div>
</template>

<script>
import Admin from './components/Admin.vue'
import Rss from './components/Rss.vue'
import podcasts from './DndPodcasts.json'

export default {
  name: 'App',
  components: {
    Rss
  },
  mounted() {
    Rss.feeds = podcasts;
    Admin.feeds = podcasts;
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
