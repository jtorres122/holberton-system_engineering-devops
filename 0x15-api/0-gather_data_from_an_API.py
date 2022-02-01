#!/usr/bin/python3
'''
Module gathers data from a REST API, for a given employee ID, and
returns information about his/her list progress
'''


from requests import get
import json
from sys import argv

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/users"
    employee_ID = int(argv[1])
    request = get(url)
    users = request.text
    data = json.loads(users)
    employee_name = data[employee_ID]

    print("Employee {}".format(employee_name))
