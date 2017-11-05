#!/bin/sh
if [ -z "$1" ]
	then # Only download and extract a single directory
		curl -s https://api.github.com/repos/scalation/data/releases/latest \
		| grep browser_download_url \
		| sed -e "s/      \"browser_download_url\": //" \
		| xargs wget -q -O - \
		| tar -xzv 
	else # Download data from all directories
		curl -s https://api.github.com/repos/scalation/data/releases/latest \
		| grep browser_download_url \
		| grep $1 \
		| sed -e "s/      \"browser_download_url\": //" \
		| xargs wget -q -O - \
		| tar -xzv 
fi