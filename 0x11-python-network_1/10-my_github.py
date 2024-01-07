#!/usr/bin/python3
"""Sends a search request for a given string to the Star Wars API"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    auth = (username, password)
    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        user_info = response.json()
        print(user_info['id'])
    except requests.exceptions.HTTPError as e:
        print(None)
