#!/usr/bin/python3
import requests
"""  a function that queries the Reddit API and
returns the number of subscribers for a given subredit"""


def number_of_subscribers(subreddit):

    """
    Returns the number of subscribers for
    the subreddit, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    """ Setting a custom User-Agent to prevent Too Many Requests errors"""
    headers = {'User-Agent': 'Vagrant/1.0 (Ken_E)'}
    """ Making the GET request to the Reddit API"""
    response = requests.get(url, headers=headers)
    """ Checking if the request was successful (status code 200) """
    if response.status_code == 200:
        """ Parsing the JSON response to get the number of subscribers """
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        """ returning 0 if invalid """
        return 0
