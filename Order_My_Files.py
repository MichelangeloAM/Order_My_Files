import glob
import os
import tkinter.filedialog
import pathlib
from datetime import datetime
from os import rename
from tkinter import simpledialog
import getpass
import time


# File types list
ftypes = [
    ('Python code files', '*.py'),
    ('Perl code files', '*.pl;*.pm'),
    ('Java code files', '*.java'),
    ('C++ code files', '*.cpp;*.h'),
    ('Text files on mac', '*.rtf'),
    ('Text files', '*.txt'),
    ("PDF files", "*.pdf"),
    ('All files', '*'),
]


root = tkinter.Tk()

# Window to select files to order
filez = tkinter.filedialog.askopenfilenames(parent=root, title='Select files to rename (must be all of the same type!)')

'''
for line in filez:
    time.ctime(os.path.getctime(line))
'''

# List populated with file names
lst = list(filez)

# Saves the extension of the selected files
suffix = pathlib.Path(lst[1]).suffix


# Window to get user input on file naming
root = tkinter.Tk()
root.geometry("400x240")

ROOT = tkinter.Tk()

ROOT.withdraw()

USER_INP = simpledialog.askstring(title="Test", prompt="Name your files:")

# Gets username for path use
username = getpass.getuser()

name = USER_INP
num = 1

USER_INP2 = simpledialog.askstring(title="Test", prompt="Name your folder:")

foldername = USER_INP2

# Creates new folder for ordered files, if folder exists, it uses it
newpath = r'/Users/' + username + '/Desktop/' + foldername + '/'
if not os.path.exists(newpath):
    os.makedirs(newpath)

lst.sort(key=os.path.getmtime)

# Renames and relocates selected files
for line in lst:
    dst = newpath + name + str(num) + suffix
    rename(line, dst)
    num += 1
#file_list = os.listdir(newpath)

