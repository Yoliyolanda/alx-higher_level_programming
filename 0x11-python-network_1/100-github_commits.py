#!/usr/bin/python3
"""This Python script takes 2 arguments in order to solve the  challenge that list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails” 
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
