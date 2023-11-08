#!/usr/bin/python3
""" a recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a
sorted count of given keywords """

import requests

def count_words(subreddit, word_list, after=None, word_counts=None):
    """
    Prints a sorted count of keywords.

    Args:
    subreddit (str): The name of the subreddit to query.
    word_list (list): A list of keywords to count.
    after (str): The "after" parameter for pagination (used for recursion).
    word_counts (dict): A dictionary to store word counts (used for recursion).

    Returns:
    None
    """
    """ Initializing the word_counts dictionary on the first call """
    if word_counts is None:
        word_counts = {}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"

    headers = {'User-Agent': 'Vagrant/1.0 (Ken_E)'}

    """Making a request """
    response = requests.get(url, headers=headers)

    """ Checking if the request was successful (status code 200) """
    if response.status_code == 200:
        """ Parsing the JSON response to get the titles of the hot posts """
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            for word in word_list:
                """ Checking if the word is found in the title (case-insensitive) """
                if word.lower() in title.lower():
                    """ Updating the word count in the dictionary """
                    word_counts[word] = word_counts.get(word, 0) + 1

        """ Checking for more pages to fetch if they exist """
        after = data['data']['after']
        if after is not None:
            """ Recursively calling the function with the updated parameters """
            return count_words(subreddit, word_list, after, word_counts)
        else:
            """ Sorting and printing the word counts in descending order """
            sorted_counts = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
            for word, count in sorted_counts:
                print(f"{word.lower()}: {count}")
    else:
        """ If the subredit is Invalid """
        return None
