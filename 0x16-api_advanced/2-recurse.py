#!/usr/bin/python3
"""
   get all hot titles for a subreddit
   using recursion
"""
import requests as re
after = None


def recurse(subreddit, hot_list=[]):
    """returning list of top ten
      post titles recursively
    """

    global after
    user_agent = {'User-agent': 'Google Chrome Version 120.0.0.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = re.get(url, params=parameters, headers=user_agent,
                     allow_redirects=False)

    if results.ok:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
