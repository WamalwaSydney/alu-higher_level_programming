#!/bin/bash
# Send GET request with required header
curl -sL -H "X-HolbertonSchool-User-Id: 98" -H "Content-Type: application/json" "$1"
