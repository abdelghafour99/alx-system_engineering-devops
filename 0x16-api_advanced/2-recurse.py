#!/usr/bin/python3
"""
Recursive function that queries the Reddit API
    & returns a list
        containing the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively retrieves a list of titles
        of all hot posts on a given subreddit
    & Returns
            A list of post titles from the hot section of the subreddit
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after}
    headers = {"User-Agent": "My-User-Agent"}

    response = requests.get(url, params=params,
                            headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])
    after = data.get("after", None)

    if not children:
        return None if not hot_list else hot_list

    hot_list.extend([child["data"]["title"] for child in children])

    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
