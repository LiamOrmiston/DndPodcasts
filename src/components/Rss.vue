<template>
  <div class="rss">
    <h1>{{ test }}</h1>
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
  }
}
</script>
