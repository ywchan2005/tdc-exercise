#!/bin/bash

name=tdc

docker rm -f $name
docker run -it --name $name $name
