#!/bin/bash
# This script sends a request to the provided URL and returns the size of the body of the response
curl -s "${1}" | wc -c
