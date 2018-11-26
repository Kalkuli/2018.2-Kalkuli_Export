#!/bin/bash

set -e
set -u

#Heroku Deploy

if [ $TRAVIS_PULL_REQUEST != "false" -o $TRAVIS_BRANCH != "master" ]
then
    echo "Skipping deployment on branch=$TRAVIS_BRANCH, PR=$TRAVIS_PULL_REQUEST"
    exit 0;
fi

docker login -u _ -p "$HEROKU_TOKEN" registry.heroku.com

docker build -t registry.heroku.com/kalkuli-export/web -f Dockerfile-prod .

docker push registry.heroku.com/kalkuli-export/web

heroku container:release web -a kalkuli-export


# Zappa Deploy

# if [ $TRAVIS_PULL_REQUEST = "false" -a $TRAVIS_BRANCH = "develop" ]
# then
#     echo "Deploy on homologation environment started"
#     pip3 install zappa
#     zappa update hom
#     echo "Deploy on homologation environment finished"
#     exit 0;
# fi

# if [ $TRAVIS_PULL_REQUEST = "false" -a $TRAVIS_BRANCH = "master" ]
# then
#     echo "Deploy on production environment started"
#     pip3 install zappa
#     zappa update prod
#     echo "Deploy on production environment finished"
#     exit 0;
# fi


# echo "Skipping deployment on branch=$TRAVIS_BRANCH, PR=$TRAVIS_PULL_REQUEST"


