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
    r = requests.get(url, headers=headers, allow_redirects=False,
                     params={"after": after})

    if r.status_code == 200:
        hot_list.extend(get_titles(r.json()['data']['children']))
        after = r.json()['data']['after']
        if after is not None:
            return get_posts(url, hot_list, after)
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
