#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (compatible; My-Unique-User-Agent/0.1)"}

    try:
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check for response errors
        if response.status_code != 200:
            return 0

        # Check if response is empty
        if response.text == "":
            return 0

        # Parse the response and return the subscriber count
        data = response.json().get("data")
        if data is not None:
            return data.get("subscribers", 0)
        else:
            return 0

    except requests.RequestException as e:
        # Handle any exceptions during the request
        print(f"Request error: {e}")
        return 0

    except ValueError:
        # Handle JSON decoding errors
        print("Error decoding the response as JSON")
        return 0
