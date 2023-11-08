#!/usr/bin/python3
""" A recursive function that queries the Reddit
API and returns a list containing the titles of
all hot articles for a given subreddit.  """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list of titles of all hot articles for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit to query.
    hot_list (list): A list to store the titles of hot articles
    after (str): The "after" parameter for paginatio).
    Returns:
    list: A list containing the titles of hot articles, or None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"    
    headers = {'User-Agent': 'vagrant/1.0 (Ken_E)'}
    
    """ Making a request """
    response = requests.get(url, headers=headers)
    
    """ Checking if the request was successful """
    if response.status_code == 200:
        """ Parsing the JSON response to get the titles of the hot posts """
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        
        """ Checking if there are more pages to fetch """
        after = data['data']['after']
        if after is not None:
            """ Recursively calling the function with the updated "after" parameter """
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        """ Invalid subreddit or other error, return None """
        return None
