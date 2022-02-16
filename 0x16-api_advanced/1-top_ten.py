#!/usr/bin/python3
'''
Function that queries the Reddit API and returns
the top 10 posts for a given subreddit
'''
import json
import requests


def top_ten(subreddit):
    url = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                       .format(subreddit),
                       headers={'User-agent': 'your bot 0.1'})

    if url.status_code == 404:
        print(None)
    else:
        data = url.json().get("data").get("children")
        for idx in data:
            print(idx.get("data").get("title"))
