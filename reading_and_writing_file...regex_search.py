'''
Search the text in a file based on a regex
'''

import re
import os
from pathlib import Path, PosixPath


def regex_folder_search(path: PosixPath, regex: re.Pattern) -> dict:
    '''
    Search the text in a file based on a regex
    Parameters:
    path
    regex
    '''
    result = {}

    for file_path_obj in path.glob('*.py'):
        file = open(file_path_obj, 'r', encoding='utf-8')
        file_content = file.read()
        search = regex.search(file_content)
        if search:
          result[os.path.basename(file_path_obj)] = search.group()
    return result


print(regex_folder_search(Path('/home/arslan/Documents/programs'),
      re.compile(r'print\((\d+|\w+|\D+|\W+)\)')))
