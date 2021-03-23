import os
import tkinter.filedialog
import pathlib
from os import rename
from tkinter import simpledialog
import getpass

root = tkinter.Tk()

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


def hide(root):
    root.iconify()


def show(root):
    root.update()
    root.iconify()


def close():
    root.destroy()


def buttons():
    root.geometry('400x400')
    root.title('Select Ordering Mode')


    btncreation = tkinter.Button(root, text='Order by Creation',
                                 command=lambda: [creation(), close()])
    btncreation.pack(side='top')
    btncreation.place(relx=0.5, rely=0.0, anchor='n')

    btnmodified = tkinter.Button(root, text='Order by Last Modified',
                                 command=lambda: [lastmodified(), close()])
    btnmodified.pack(side='top')
    btnmodified.place(relx=0.5, rely=0.5, anchor='center')

    btnaccessed = tkinter.Button(root, text='Order by Last Accessed',
                                 command=lambda: [lastaccessed(), close()])
    btnaccessed.pack(side='top')
    btnaccessed.place(relx=0.5, rely=1.0, anchor='s')

hide(root)

# Window to select files to order
filez = tkinter.filedialog.askopenfilenames(title='Select files to rename (must be all of the same type!)')

# List populated with file names
lst = list(filez)

# Saves the extension of the selected files
suffix = pathlib.Path(lst[0]).suffix

# Window to get user input on file naming

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

show(root)
buttons()


root.mainloop()