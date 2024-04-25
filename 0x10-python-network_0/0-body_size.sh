#!/bin/bash
# Return the number of bytes downloaded
curl -s -w "%{size_download}" "$1"
