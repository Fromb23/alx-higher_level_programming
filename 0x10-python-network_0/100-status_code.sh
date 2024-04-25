#!/bin/bash
# Script that sends a request to a URL and displays the code status
curl -so /dev/null -w "%{http_code}" "$1"
