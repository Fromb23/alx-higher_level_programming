#!/bin/bash
# Return the number of bytes downloaded
curl -sI "$1" | grep "content-Length:" | cut -d " " -f 2
