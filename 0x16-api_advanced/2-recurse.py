
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
    # Construct the URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Define parameters for the request, including pagination and limit
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    # Send a GET request to the subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the response status code indicates a not-found error (404)
    if response.status_code == 404:
        return None
    # Parse the JSON response and extract relevant data
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    # Append post titles to the hot_list
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    # If there are more posts to retrieve, recursively call the function
    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    # Return the final list of hot post titles
    return hot_list
