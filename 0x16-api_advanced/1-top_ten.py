#!/usr/bin/python3
"""
Function that queries the Reddit API
    & prints the titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """ Print the titles of the 10 hottest posts on a given subreddit """

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    head = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    para = {
        "limit": 10
    }

    resp = requests.get(url, head=head, para=para,
                            allow_redirects=False)

    if resp.status_code == 404:
        print("None")
        return

    resul = resp.json().get("data")

    [print(c.get("data").get("title")) for c in resul.get("children")]
