#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """ queries the Reddit API and returns the number of subscribers \
    (not active users, total subscribers) for a given subreddit.

    Args:
        subreddit (str): subreddit
    """
    headers = {'User-Agent': 'Reddit API calls by Lewis'}
    r = requests.get(
        f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers)

    if r.status_code == 200:
        subs_count = r.json()['data']['subscribers']
        return subs_count
    
    return 0
