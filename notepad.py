from tkinter import *
from tkinter import filedialog
root=Tk()
e=Entry(root).place(width=10000,height=1000)
root.title=('notepad')
root.configure(background='light blue')
def savefile():
    file_save=filedialog.asksaveasfile(mode='w',defaultextension='txt')
button=Button(root,text='save file',command=savefile).pack()

root.mainloop()


