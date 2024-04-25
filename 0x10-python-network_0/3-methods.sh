#!/bin/bash
# Takes a URL and displays all the HTTP methods
curl -sI "$1" | grep "Allow"
