module.exports = {
  pages: {
    index: {
      entry: 'src/main.js',
      template: 'public/index.html',
      filename: 'index.html',
      title: 'Dnd Podcasts',
    }
  },
  publicPath: process.env.NODE_ENV === 'production'
    ? '/DndPodcasts/'
    : '/'
}
