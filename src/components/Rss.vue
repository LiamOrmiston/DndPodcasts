<template>
  <div class="rss">
    <b-container class="podcastContainer">
      <b-card 
        class="podcastCard"
        v-for="post in posts.slice((currentPage - 1) * perPage, currentPage * perPage)"
        v-bind:key="post.id"
      >
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
      <b-pagination 
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        aria-controls="podcastContainer"
        align="center"
      ></b-pagination>
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
      currentPage: 1,
      perPage: 5
    }
  },
  computed: { 
    rows() { 
      return this.posts.length
    }
  },
  mounted() {
    this.posts = podcasts['podcasts'];
  }
}
</script>
<style src="./Rss.css" scoped>
</style>
