#!/usr/bin/python3
"""This Python script fetches https://alx-intranet.hbtn.io/status"""
import requests

response = requests.get('https://alx-intranet.hbtn.io/status')
data = response.json()

print("Body response:")
print("\t- type:", type(data))
print("\t- content:", data)

