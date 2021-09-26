"""Удаление файла .json"""
__name__ = 'delete'

__all__ = ['delete_json']

import os


def delete_json(path, file_name):
    os.remove(path + '\\' + file_name + '.json')
