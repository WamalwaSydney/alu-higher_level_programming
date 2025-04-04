#!/bin/bash
# Display body only for status code 200
[ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" = "200" ] && curl -sL "$1"
