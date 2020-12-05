<template>
  <div class="rss">
    <b-container class="podcast-card">
      <b-card v-for="post in posts" v-bind:key="post.id">
        <b-row no-gutters>
          <b-col md="2">
            <a v-bind:href="post.link">
              <b-img v-bind:src="post.image" rounded fluid></b-img>
            </a>
          </b-col>
          <b-col fluid>
            <b-card-body v-bind:title="post.title">
              <b-card-text>
                <div v-html="post.content"></div>
              </b-card-text>
            </b-card-body>
          </b-col>
        </b-row>
      </b-card>
    </b-container>
  </div>
</template>

<script>
import podcasts from '../data.json'

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
