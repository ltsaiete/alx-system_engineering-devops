#!/usr/bin/python3
"""This is a simple module and it only has
one function called recurse
"""
import requests


def get_titles(posts):
    """Extract the titles of the posts

    Args:
        posts (_type_): _description_

    Returns:
        _type_: _description_
    """
    titles = []
    for post in posts:
        titles.append(post['data']['title'])
    return titles


def get_posts(url, hot_list=[], after=None):
    """Get the posts

    Args:
        url (_type_): _description_
        hot_list (list, optional): _description_. Defaults to [].
        after (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    headers = {'User-Agent': 'Reddit API calls by Lewis'}

    if after is None:
        r = requests.get(url, headers=headers)
    else:
        r = requests.get(f'{url}?after={after}', headers=headers)

    if r.status_code == 200:
        hot_list.extend(get_titles(r.json()['data']['children']))
        if r.json()['data']['dist'] == 25:
            return get_posts(url, hot_list, r.json()['data']['after'])
    else:
        return None

    return hot_list


def recurse(subreddit, hot_list=[]):
    """this is a recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): subreddit
    """

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    return get_posts(url)
