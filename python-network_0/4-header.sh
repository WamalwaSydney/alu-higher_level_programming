#!/bin/bash
# Script that sends a GET request with a specific header
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
