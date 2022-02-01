#!/usr/bin/python3
'''
Module gathers data from a REST API, for a given employee ID, and
returns information about his/her list progress
'''

import csv
import json
from requests import get
from sys import argv


if __name__ == "__main__":

    employee_ID = int(argv[1])
    num_of_tasks = 0
    num_of_tasks_done = 0

    users_url = "https://jsonplaceholder.typicode.com/users"
    users_request = get(users_url)
    users = users_request.text
    users_data = json.loads(users)

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_request = get(todos_url)
    todos = todos_request.text
    todos_data = json.loads(todos)

    with open('{}.csv'.format(employee_ID), 'w') as f:
        for todo in todos_data:
            for user in users_data:
                if user['id'] == employee_ID and\
                  todo['userId'] == employee_ID:
                    f.write('"{}","{}","{}","{}"\n'.format(employee_ID,
                                                           user['username'],
                                                           todo['completed'],
                                                           todo['title']))
