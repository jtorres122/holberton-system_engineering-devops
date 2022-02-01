#!/usr/bin/python3
'''
Module gathers data from a REST API, for a given employee ID, and
returns information about his/her list progress
'''

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

    for count in todos_data:
        if count['userId'] == employee_ID and\
          count['completed'] is True:
            num_of_tasks_done += 1
            num_of_tasks += 1
        if count['userId'] == employee_ID and\
           count['completed'] is False:
            num_of_tasks += 1

    for d in users_data:
        if d['id'] == employee_ID:
            print("Employee {} is done with tasks({}/{}):"
                  .format(d['name'],
                          num_of_tasks_done,
                          num_of_tasks))

    for title in todos_data:
        if title['userId'] == employee_ID and\
          title['completed'] is True:
            print("\t {}".format(title['title']))
