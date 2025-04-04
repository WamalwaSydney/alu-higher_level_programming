#!/bin/bash
# Fetch and display the body of a response if HTTP status code is 200
curl -sL "$1" -o tmp_response && [ "$(tail -c 3 tmp_response)" = "200" ] && head -c -3 tmp_response && echo ""
