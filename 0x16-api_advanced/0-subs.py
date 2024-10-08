#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the total number of subscribers for a given subreddit.
    If the subreddit is invalid, return 0.
    """

    # Define the URL to access the subreddit information
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set a custom User-Agent to avoid being blocked by Reddit
    headers = {"User-Agent": "Mozilla/5.0 (compatible; My-Unique-User-Agent/0.1)"}

    try:
        # Make a GET request to Reddit API with the given URL and custom headers
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check for 404 (subreddit not found) or other errors
        if response.status_code != 200:
            return 0

        # Parse the response as JSON and get the "data" field
        data = response.json().get("data")
        
        # Return the number of subscribers, or 0 if the "data" field is not found
        if data:
            return data.get("subscribers", 0)
        else:
            return 0

    except requests.RequestException:
        # If any request-related error occurs, return 0
        return 0

