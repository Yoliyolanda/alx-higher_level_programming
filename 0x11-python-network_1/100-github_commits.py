#!/usr/bin/python3
"""This Python script takes 2 arguments in order to solve the  challenge that list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails” """
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
