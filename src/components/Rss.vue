<template>
  <div class="rss">
    <ul class="posts-sidebar">
      <li
        v-for="post in posts"
        v-bind:key="post.id"
        v-bind:class="{ selected: post === selectedPost }"
        v-on:click="selectedPost = post"
      >
        {{ post.title }}
      </li>
    </ul>
    <div class="selected-post-container">
      <div
       v-if="selectedPost"
       class="selected-post"
      >
        <h3>{{ selectedPost.title }}</h3>
        <a v-bind:href="selectedPost.link">
          <img v-bind:src="selectedPost.image" width="200" height="200">
        </a>
        <div v-html="selectedPost.content"></div>
      </div>
      <strong v-else>
        Click on a Podcast to the left to view its description.
      </strong>
    </div>
  </div>
</template>

<script>
import podcasts from '../data.json'
// import podcasts from '../DndPodcasts.json'

export default {
  name: 'Rss',
  props: {
    feed: Array
  },
  data: function () {
    return {
      posts: [],
      selectedPost: null
    }
  },
  mounted() {
    this.posts = podcasts['podcasts'];
  }
}
</script>
<style src="./Rss.css" scoped>
</style>
