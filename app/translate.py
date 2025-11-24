import json
import os

DEFAULT_LANGUAGE ='en'

def trans():
    trans_file_path = os.path.join('./static/i18n', DEFAULT_LANGUAGE+'.json')
    print(trans_file_path)
    with open(trans_file_path, 'r') as file:
        content= file.read()
        __trans = json.loads(content)
        return __trans

def translate():
   _trans = trans()
   def call_back(path):
    nonlocal _trans
    return _trans[path]
   return call_back