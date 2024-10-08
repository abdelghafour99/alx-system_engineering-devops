#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    head = {"User-Agent": "My-Unique-User-Agent"}

    resp = requests.get(url, headers=head, allow_redirects=False)

    if resp.status_code != 200:
        return 0

    data = resp.json().get("data", {})
    return data.get("subscribers", 0)
