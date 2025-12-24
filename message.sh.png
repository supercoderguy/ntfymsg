#!/bin/bash

python config.py
username=$(cat config)

echo "Enter message:"
read message
curl -d "$username says: $message" ntfy.sh/onlinemessaging

