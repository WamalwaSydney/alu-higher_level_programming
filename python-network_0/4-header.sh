#!/bin/bash
# Send GET request with required header and force response check
curl -sL -H "X-HolbertonSchool-User-Id: 98" -H "Accept: */*" "$1"
