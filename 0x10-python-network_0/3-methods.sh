#!/bin/bash
# Takes a URL and displays all the HTTP methods
curl -sX OPTIONS -I "$1" | grep "Allow:" | cut -d " " -f 2-
