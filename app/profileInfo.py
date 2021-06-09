from flask import json


def get_profile_data(filename):

    with open(filename) as file:
        data = json.load(file)
        return data
