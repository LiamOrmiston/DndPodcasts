<template>
  <div class="admin">
    <form v-on:submit.prevent="addNewFeed">
      <label for="new-feed">Add a feed</label>
      <input
        v-model="newFeedText"
        id="new-feed"
        placeholder="E.g. Art of the Roll"
      >
      <button>Add</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'Admin',
  props: {
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
}
</script>
