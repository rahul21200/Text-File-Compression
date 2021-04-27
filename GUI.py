from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
from Huffman import *
gui = Tk()
gui.geometry("400x100")
gui.configure(bg = "yellow")
gui.title("File Compressor")


def getFolderPath():
    folder_selected = filedialog.askopenfile(initialdir = "/")
    file_path = folder_selected.name
    folderPath.set(folder_selected)
    return file_path


def doStuff():
    file = folderPath.get()
    fpath = getFolderPath()
    H = HuffmanCoding(fpath)
    H.compress()
    print("Compressed to", fpath.replace("txt","bin"))

# def doStuff2():
#     file = folderPath.get()
#     fpath = getFolderPath()
#     H = HuffmanCoding(fpath)
#     H.decompress(fpath)
#     print("Decompressed to", fpath.replace(".bin","_decompressed.txt"))


folderPath = StringVar()
a = Label(gui ,text="Enter path",bg = "yellow")
a.grid(row=0,column = 0)
E = Entry(gui,textvariable=folderPath)
E.grid(row=0,column=1)

c = ttk.Button(gui ,text="Browse File for compression", command=doStuff)
c.grid(row=0,column=2)
# c = ttk.Button(gui ,text="Browse File for decompression", command=doStuff2)
# c.grid(row=1,column=2)
gui.mainloop()