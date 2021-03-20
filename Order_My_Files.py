import glob
import os
import tkinter.filedialog
import pathlib
from os import rename
from tkinter import simpledialog
import getpass

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

# The function renames and relocates selected files depending on the sorting selected


def creation():
    lst.sort(key=os.path.getctime)
    num = 1
    for line in lst:
        dst = newpath + name + str(num) + suffix
        rename(line, dst)
        num += 1


def lastmodified():
    lst.sort(key=os.path.getmtime)
    num = 1
    for line in lst:
        dst = newpath + name + str(num) + suffix
        rename(line, dst)
        num += 1


def lastaccessed():
    lst.sort(key=os.path.getatime)
    num = 1
    for line in lst:
        dst = newpath + name + str(num) + suffix
        rename(line, dst)
        num += 1



root = tkinter.Tk()

# Window to select files to order
filez = tkinter.filedialog.askopenfilenames(parent=root,
                                            title='Select files to rename (must be all of the same type!)')

'''
for line in filez:
    time.ctime(os.path.getctime(line))
'''

# List populated with file names
lst = list(filez)

# Saves the extension of the selected files
suffix = pathlib.Path(lst[0]).suffix


# Window to get user input on file naming
root = tkinter.Tk()
root.geometry("400x240")

ROOT = tkinter.Tk()

ROOT.withdraw()

# Asks user for file names, while loop won't break if no name is given
USER_INP = simpledialog.askstring(title="File Names",
                                  prompt="Name your files:")

while USER_INP == '':
    USER_INP = simpledialog.askstring(title="File Names",
                                      prompt="Name your files:")

# Gets username for path use
username = getpass.getuser()

name = USER_INP

# Asks user for folder name, while loop won't break if no name is given
USER_INP2 = simpledialog.askstring(title="Folder Name",
                                   prompt="Name your folder:")

while USER_INP2 == '':
    USER_INP2 = simpledialog.askstring(title="Folder Name",
                                       prompt="Name your folder:")

foldername = USER_INP2

# Creates new folder for ordered files, if folder exists, it uses it
newpath = r'/Users/' + username + '/Desktop/' + foldername + '/'
if not os.path.exists(newpath):
    os.makedirs(newpath)

user_input3 = simpledialog.askstring(title="Mode",
                                     prompt="Write: c to order by creation, m by last modified, a by last accessed")

while user_input3 != 'c' and user_input3 != 'm' and user_input3 != 'a':
    user_input3 = simpledialog.askstring(title="Mode",
                                         prompt="Write: c to order by creation, m by last modified, a by last accessed")

if user_input3 == 'c':
    creation()
elif user_input3 == 'm':
    lastmodified()
else:
    lastaccessed()