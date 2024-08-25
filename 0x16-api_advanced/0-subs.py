#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    head = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, head=head, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        subscr = data['data']['subscribers']
        return subscr
    else:
        return 0
