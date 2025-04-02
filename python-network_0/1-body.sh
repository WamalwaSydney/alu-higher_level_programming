#!/bin/bash
# Script that displays the body of a 200 status code response
curl -s -w "%{http_code}" "$1" | grep -A1 "200" | tail -n 1
