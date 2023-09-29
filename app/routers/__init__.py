from pathlib import Path
from os import listdir
from importlib import import_module
path_parent = Path('./app/routers')
# print(listdir(path_parent))
for module in listdir(path_parent):
  if 'router' in module:
    # print(module [:-3])
    # print(module [:-3])
    import_module(f'app.routers.{module[:-3]}')
    
