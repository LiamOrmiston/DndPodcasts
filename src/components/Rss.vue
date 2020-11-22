<template>
  <div class="rss">
    <b-card-group deck>
      <b-card no-body class="overflow-auto" style="max-width: 540px; max-height: 250px;" v-for="post in posts" v-bind:key="post.id">
        <b-row no-gutters>
          <b-col md="6">
            <a v-bind:href="post.link">
              <b-card-img v-bind:src="post.image" class="rounded-0"></b-card-img>
            </a>
          </b-col>
          <b-col md="6">
            <b-card-body v-bind:title="post.title">
              <b-card-text>
                <div v-html="post.content" style="text-overflow: ellipsis;"></div>
              </b-card-text>
            </b-card-body>
          </b-col>
        </b-row>
      </b-card>
    </b-card-group>
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
