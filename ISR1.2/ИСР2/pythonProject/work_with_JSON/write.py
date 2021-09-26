"""Запись в файл .json"""
__name__ = 'write'

__all__ = ['write_json']

import json


def write_json(dict, path, file_name):
    file = open(path + '\\' + file_name + '.json', 'x')
    file.write(json.dumps(dict, separators=(',', ':')))
    file.close()

