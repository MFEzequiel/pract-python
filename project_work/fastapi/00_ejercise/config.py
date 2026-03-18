import sys
import os
from pathlib import Path
import json

def dir_path(dir, new_path):
  return os.path.join(dir, new_path)

# directorio actual del archivo config
cwd = os.getcwd()
directory = os.path.dirname(__file__)
dir_file = dir_path(cwd, 'archivos')
dir_json = dir_path(cwd, 'json')
folder_files_excel = dir_path(dir_file, 'excel')

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = directory

template_path = os.path.join(base_path, "server", "templates")

def create_folder():
  for directory in [dir_file, folder_files_excel, dir_json]:
    if not os.path.exists(directory):
      os.makedirs(directory)
  
file_json = dir_path(dir_json, 'courses.json')

if not os.path.exists(file_json):
  data = {"body": []}
  
  with open(file_json, "w") as f:
      json.dump(data, f, indent=4)