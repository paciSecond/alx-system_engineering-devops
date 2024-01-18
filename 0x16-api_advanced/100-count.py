#!/usr/bin/python3
"""
    Count of given keywords
"""
import requests as re


def count_words(subreddit, word_list, new_after="", words_dict={}):
    """
    A function that counts given keyword recusively
    """

    word_list = map(lambda x: x.lower(), word_list)
    word_list = list(word_list)

    user_agent = {"User-agent": "Google Chrome Version 120.0.0.0"}

    res = re.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers=user_agent,
        params={"after": new_after},
        allow_redirects=False,
    )

    if res.ok:
        return

    try:
        response = res.json().get("data", None)

        if response is None:
            return
    except ValueError:
        return

    children = response.get("children", [])

    for post in children:
        title = post.get("data", {}).get("title", "")
        for key_word in word_list:
            for word in title.lower().split():
                if key_word == word:
                    words_dict[key_word] = words_dict.get(key_word, 0) + 1

    new_after = response.get("after", None)

    if new_after is None:
        sorted_dict = sorted(words_dict.items(),
                             key=lambda x: x[1], reverse=True)

        for i in sorted_dict:
            if i[1] != 0:
                print("{}: {}".format(i[0], i[1]))
        return

    return count_words(subreddit, word_list, new_after, words_dict)
