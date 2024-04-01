import os
import shutil

from_dir="C102_assets-main"
to_dir="C102_assets-main"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,extention=os.path.splitext(file_name)
    print(name),print(extention)