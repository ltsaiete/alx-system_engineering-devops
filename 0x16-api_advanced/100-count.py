#!/usr/bin/python3
"""This is a simple module and it only has
one function called count_words
"""
import requests


def count_words(subreddit, word_list):
    """a recursive function that queries the Reddit API, parses the title of
    all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces. Javascript should
    count as javascript, but java should not).

    Args:
        subreddit (_type_): _description_
        word_list (_type_): _description_
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    posts = get_posts(url)
    count_dict = {}
    word_list = [word.lower() for word in word_list]

    posts_words = [word for post in posts for word in post.split()]

    for word in posts_words:
        if word in word_list:
            if word not in count_dict:
                count_dict[word] = 0
            for w in word_list:
                if w == word:
                    count_dict[word] = count_dict[word] + 1

    key_sorted_items = sorted(count_dict.items())
    key_sorted_dict = dict(key_sorted_items)
    sorted_items = sorted(key_sorted_dict.items(),
                          key=lambda item: item[1], reverse=True)

    for k, v in sorted_items:
        print(f'{k}: {v}')


def get_titles(posts):
    """Extract the titles of the posts

    Args:
        posts (_type_): _description_

    Returns:
        _type_: _description_
    """
    titles = []
    for post in posts:
        titles.append(post['data']['title'].lower())
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
