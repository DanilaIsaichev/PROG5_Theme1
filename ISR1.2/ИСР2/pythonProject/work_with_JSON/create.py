"""Создание файла .json"""
__name__ = 'create'

__all__ = ['create_json']

def create_json(path, file_name):
    file = open(path + '\\' + file_name + '.json', 'w')
    file.close()

