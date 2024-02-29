#!/bin/bash
# This script sends a request to the provided URL using curl in silent mode
curl sI "$1" | grep -i Content-Length | awk '{print $2}'
