#!/bin/bash
# Send GET request with required header and display response body
curl -sL -H "X-HolbertonSchool-User-Id: 98" "$1"
