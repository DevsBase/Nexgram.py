import importlib.util
import os

def import_all(folder_path):
  for file in os.listdir(folder_path):
    if file.endswith(".py") and file != "__init__.py":
      module_name = file[:-3]
      module_path = os.path.join(folder_path, file)
      spec = importlib.util.spec_from_file_location(module_name, module_path)
      module = importlib.util.module_from_spec(spec)
      spec.loader.exec_module(module)
  return 