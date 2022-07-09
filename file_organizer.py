from operator import contains
from pathlib import Path
import os
import shutil


def move_files_if_japan():
    fp = Path.cwd()
    jp_fp = fp / Path("jp_files") 
    for i in os.scandir(fp):
        filename = str(i)
        if filename.find("japan") == -1:
            next
        elif filename != -1 :
            print(i)
            shutil.move(i,jp_fp)
            
def move_files_if_7z(fp = Path.cwd):
    zp_fp = fp / Path("7z_files")
    for i in os.scandir(fp):
        filename = str(i)
        if filename.endswith(".7z", ".zip"):
            print("moving " + str(i) + " to " str(zp_fp))
            shutil.move(i, zp_fp)


move_files_if_7z()
