#!/usr/bin/python3
'''
Function that queries the Reddit API and returns
the total # of subscribers for a given subreddit
'''
import json
import requests


def number_of_subscribers(subreddit):
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit),
                       headers={'User-agent': 'your bot 0.1'})
    text = url.text
    data = json.loads(text)

    if url.status_code == 404:
        return 0
    else:
        return data['data']['subscribers']
