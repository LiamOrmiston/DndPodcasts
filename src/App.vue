<template>
  <div id="app">
    <h2>DndPodcasts.com</h2>
    <Rss/>
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

<style src="./App.css">
</style>
