import feedparser
import json
data = {}
rssFeeds = []
data['podcasts'] = []
with open("dndPodcasts.txt", "r") as myFile:
    rssFeeds = myFile.read().split()
for idx, rssFeed in enumerate(rssFeeds):
    PodFeed = feedparser.parse(rssFeed)
    entry = PodFeed.entries[0]
    myFeed = PodFeed.feed
    myTitle = myFeed.title
    myDescription = myFeed.subtitle
    myLink = myFeed.links[0].href
    myImage = myFeed.image.href
    data['podcasts'].append({
        'id': idx,
        'title': myTitle,
        'content': myDescription,
        'image': myImage,
        'link': myLink
    })
with open('../data.json', 'w') as outfile:
    json.dump(data, outfile)
