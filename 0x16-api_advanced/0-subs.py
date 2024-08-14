#!/usr/bin/python3
"""
A function that queries the Reddit API and returns number of subscribers
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of sbscribers (not active
    users, total subscribers) for a given subreddit.

    Args:
        Subreddit (str): The ane of the subreddit to query.

    Returns:
        int: Number of subscribers if the subreddit exists, else 0.
    """

    if not isinstance(subreddit, str) or not subreddit:
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': 'Google Chrome version 127.0.6533.99'
        }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            results = response.json()
            retrn results.get('data', {}).get('subscribers', 0)
        else:
            return 0
        except requests.RequestException:
            return 0
