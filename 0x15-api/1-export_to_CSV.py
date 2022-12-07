#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(url + 'users', params={'id': sys.argv[1]})
    data = requests.get(url + 'todos', params={'userId': sys.argv[1]})

    with open(f'{sys.argv[1]}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for d in data.json():
            row = f"{d['userId']}, {user.json()[0]['username']},\
                    {d['completed']}, {d['title']}"
            writer.writerow(row)
