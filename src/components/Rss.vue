<template>
  <div class="rss">
    <h1>{{ test }}</h1>
    <form v-on:submit.prevent="addNewFeed">
      <label for="new-feed">Add a feed</label>
      <input
        v-model="newFeedText"
        id="new-feed"
        placeholder="E.g. Art of the Roll"
      >
      <button>Add</button>
    </form>
    <p>
      This is a test.
      <ol>
        <li v-for="feed in feeds" v-bind:key="feed.id">
          {{ feed.title }}
        </li>
      </ol>
    </p>
  </div>
</template>

<script>
import podcasts from '../DndPodcasts.json'
export default {
  name: 'Rss',
  props: {
    test: String,
    feed: Array
  },
  data: function () {
    return {
      feeds: [],
      newFeedText: '',
      nextFeedId: 3
    }
  },
  methods: {
    addNewFeed: function () {
      this.feeds.push({
        id: this.nextFeedId++,
        title: this.newFeedText
      })
      this.newFeedText = ''
    }
  },
  mounted() { // when the Vue app is booted up, this is run automatically.
    this.feeds = podcasts;
  }
}
</script>
