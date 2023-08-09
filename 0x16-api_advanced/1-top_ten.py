#!/usr/bin/python3
"""This is a simple module and it only has
one function called top_ten
"""
import requests


def top_ten(subreddit):
    """this function queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): subreddit
    """
    headers = {'User-Agent': 'Reddit API calls by Lewis'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        posts = r.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
