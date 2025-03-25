#!/bin/bash
echo Enter the container id or name
read CONTAINER_ID
SOURCE="/home/doc-bd-a1/service-result"
DEST="../"
docker cp $CONTAINER_ID:$SOURCE $DEST


docker stop $CONTAINER_ID

