#!/bin/bash
# A script that takes in a URL sends a POST request to the passed URL
curl -sX POST -d "emaail=test@gmail.com&subject=I will always be here for PLD" "$1"
