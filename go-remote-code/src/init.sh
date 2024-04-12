#!/bin/sh

echo "build docker"
docker buildx build --platform linux/amd64 . -t go-remote-code --load

echo "remove stack docker"
docker stack rm go-remote-code

echo "start stack docker"
docker stack deploy -c docker-compose.yml go-remote-code