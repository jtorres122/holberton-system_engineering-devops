#!/usr/bin/python3
'''Module gathers data from an API'''
from dataclasses import dataclass
from unicodedata import name
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
