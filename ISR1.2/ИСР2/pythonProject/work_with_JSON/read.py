"""Чтение файла .json"""
__name__ = 'read'

__all__ = ['read_json']

import json


def read_json(path, file_name):
    file = open(path + '\\' + file_name + '.json', 'r')
    data = json.load(file)
    print(data)
    return data
