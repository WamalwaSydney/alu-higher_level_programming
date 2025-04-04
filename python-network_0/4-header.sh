#!/bin/bash
# Send GET request with required header
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
