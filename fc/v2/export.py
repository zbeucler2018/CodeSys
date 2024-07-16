import os
import shutil
from pathlib import Path

from utils import save

# read from env var?
PATH_TO_PRG = ""

declaration_intro = '%' + '-' * 75 + '%\n%->> Declaration\n' + '%' + '-' * 75 + '%\n'
implementation_intro = '%' + '-' * 75 + '%\n%->> Implementation\n' + '%' + '-' * 75 + '%\n'

def search_folder():
    ...
    # gets the full path to 
    # ask user what folder they want to export (default the project/all)



def search_folder():
    # get path of user specified folder. 
    # theirs would overwrite the contents if not empty
    # it also looks for a .git folder and saves the result in a global variable
    has_repo = False
    return PATH_TO_PRG





if __name__ == 'main':
    # 1. gets folder path 
    ...