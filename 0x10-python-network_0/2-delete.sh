#!/bin/bash
# Check if URL is provided as an arg
if [ $# -eq 0 ];
then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Use curl with -X opt and DELETE method to send a request to the provided URL
curl -sX DELETE "$1"
