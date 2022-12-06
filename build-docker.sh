#!/bin/bash

name=tdc

DOCKER_BUILDKIT=1 docker build -t $name -f docker/Dockerfile .
