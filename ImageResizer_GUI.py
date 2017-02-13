#!/usr/bin/python

from Tkinter import *
from tkFileDialog import *
import os
import ImageResizer as core

#Define some Variables
bgColor = "#282828"
textcol = "#999999"
FilePaths = []

def readFiles():
    Files = askopenfilenames()
    i = len(Files)
    File_Entry.delete('1.0',END)
    for i in Files:
        FilePaths.append(i)
        splitText = os.path.split(i)
        File_Entry.insert(END,splitText[1] + '\n')


def Rs_Images():
    bwidth = int(float(Width_Entry.get()))
    FilenameList = []
    files = FilePaths
    for i in files:
        FilenameList.append(i)
    core.ResizeImages(FilenameList,bwidth)


#Define Base Window Properties
root = Tk()
root.option_add("*TCombobox*Listbox*Background", '#282828')
root.option_add("*TCombobox*Listbox*Foreground", '#999999')
root.title("Image Scaler")
root.geometry("460x250")
root.configure(background=bgColor)
root.resizable(width=False, height=False)

GenType_lbl = Label(root,text="BaseWidth",fg=textcol,bg=bgColor)
GenType_lbl.place(x=20,y=20,height=20)

Width_Entry = Entry(root,fg=textcol,bg=bgColor)
#File_Entry.insert(0, "test.fga")
Width_Entry.place(x=90,y=20,height=20,width=50)


File_btn = Button(root,text="Select Images...",fg=textcol,bg=bgColor,command=readFiles)
File_btn.place(x=20,y=50,height=20)

File_Entry = Text(root,fg=textcol,bg=bgColor,padx=2,pady=2,wrap=WORD)
#File_Entry.insert(0, "test.fga")
File_Entry.place(x=20,y=90,height=100,width=420)

Create_btn = Button(root,text="Resize Images",bg=bgColor,fg=textcol,command=Rs_Images)
Create_btn.place(x=180,y=210)


root.mainloop()

