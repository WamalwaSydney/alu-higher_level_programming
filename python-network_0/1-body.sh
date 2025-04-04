#!/bin/bash
# Only display body for HTTP 200
curl -s -L -w "%{http_code}" "$1" -o tmp_response && \
[ "$(cat tmp_response | tail -c 3)" = "200" ] && head -c -3 tmp_response && echo "" || true
