#!/usr/bin/python3
"""This python script takes your GitHub credentials.
"""
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get('https://api.github.com/user',
                     auth=(argv[1], argv[2]))
    if r.status_code == 200:
        j = r.json()
        print(j.get('id'))
    else:
        print('None')
