#!/usr/bin/python3
"""
Function that queries the Reddit API
    & prints the titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """ Print the titles of the 10 hottest posts on a given subreddit """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    para = {"limit": 10}
    head = {"User-Agent": "My-Unique-User-Agent"}

    resp = requests.get(url, para=para,
                        head=head, allow_redirects=False)

    if resp.status_code != 200:
        print('None')
        return

    data = resp.json().get("data", {})
    children = data.get("children", [])

    if not children:
        print('None')
        return

    for child in children:
        print(child.get("data", {}).get("title", ''))
