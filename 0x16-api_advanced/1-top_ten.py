#!/usr/bin/python3
""" a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit. """
import requests


def top_ten(subreddit):
    """
    Prints the hot 10 posts on a given subreddit
    Args:
    subreddit (str): The name of the subreddit to query.
    Returns:
    None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    """ Setting a custom User-Agent to prevent Too Many Requests errors """
    headers = {'User-Agent': 'Ken/1.0 (Ken_b)'}

    """ Making the GET request to the Reddit API """
    response = requests.get(url, headers=headers)

    """ Checking if the request was successful (status code 200)"""
    if response.status_code == 200:
        """ Parsing the JSON response to get
        the titles of the first 10 hot posts """
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        """ If the subreddit is invalid or other error, print None """
        print(None)
