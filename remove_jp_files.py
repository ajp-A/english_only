from operator import contains
from pathlib import Path
import os
import shutil


def move_roms():
    rom_fp = Path.cwd()
    jp_fp = rom_fp / Path("jp_files") 
    for i in os.scandir(rom_fp):
        filename = str(i)
        if filename.find("japan") == -1:
            next
        elif filename != -1 :
            print(i)
            shutil.move(i,jp_fp)
            
                    

move_roms()