#!/usr/bin/env sh

# abort on errors
set -e

# build
npm run build

# navigate into the build output directory
cd dist

echo 'www.DndPodcasts.com' > CNAME

git init
git add -A
git commit -m 'deploy'

git push -f git@github.com:LiamOrmiston/DndPodcasts.git master:gh-pages

cd -
