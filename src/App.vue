<template>
  <div id="app">
    <b-container>
      <h2>DndPodcasts.com</h2>
    </b-container>
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
