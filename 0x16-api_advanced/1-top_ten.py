#!/usr/bin/python3
'''
Function that queries the Reddit API and returns
the total # of subscribers for a given subreddit
'''
import json
import requests


def top_ten(subreddit):
    url = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                       .format(subreddit),
                       headers={'User-agent': 'your bot 0.1'})
    data = url.json().get("data").get("children")

    if url.status_code == 404:
        print(None)
    else:
        for idx in data:
            print(idx.get("data").get("title"))
