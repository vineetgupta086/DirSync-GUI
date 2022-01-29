# for running shell commands
import subprocess as sp
import os

# for gui
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from PIL import ImageTk, Image

# for app update
from Updater import *
# utilites
from utils import FindFromFile, RunCommand

# global MyBg; global MyFg
try:
    MyVersion = FindFromFile("VERSION", "source/TEXTDATA")
except Exception as e:
    messagebox.INFO(title = "DirSync-GUI", message = e)

class Main:
    global RootExists
    RootExists = True
    def __init__(self, parent):
        global SourceDir; global TargetDir
        global RootExists; global e1; global e2
        RootExists = UpdateVersion(parent)
        tk.Button(parent, text = "Check for updates", fg = "#ffffff", bg = "#121212", command = lambda: UpdateVersion(parent), padx = 5).place(x = 405, y = 92)
        # self.MainOptions()
        def Entry():
            global SourceDir; global TargetDir
            global e1; global e2
            EntryFrame = tk.Frame(parent, padx = 5, pady = 5, bg = MyBg)
            EntryFrame.place(x = 10, y = 120)
            L = ["Source","Target"]
            for i in L:
                j = L.index(i)
                tk.Label(EntryFrame, fg = MyFg, bg = MyBg, text = f"{i} Directory:  ").grid(row = j, column = 0)
                tk.Label(EntryFrame, text = " "*3, fg = MyFg, bg = MyBg).grid(row = j, column = 2, columnspan = 1)
            
            e1 = tk.Entry(EntryFrame, fg = MyFg, bg = MyBg, width = 53); e1.grid(row = 0, column = 1)
            e2 = tk.Entry(EntryFrame, fg = MyFg, bg = MyBg, width = 53); e2.grid(row = 1, column = 1)

            # Textbox for taking input
            def BrowseSource():
                SourceDir = askdirectory(title = "Select The Source Directory:")
                e1.delete(0, tk.END); e1.insert(0, SourceDir)
            def BrowseTarget():
                TargetDir = askdirectory(title = "Select The Target Directory:")
                e2.delete(0, tk.END); e2.insert(0, TargetDir)

            tk.Button(EntryFrame, text = "Browse", command = BrowseSource).grid(row = 0, column = 3)
            tk.Button(EntryFrame, text = "Browse", command = BrowseTarget).grid(row = 1, column = 3)      
        if RootExists: Entry()

        def MainFrame():
            global SourceDir; global TargetDir
            global e1; global e2

            MainFrame = tk.LabelFrame(parent, text = "Main Options", padx = 5, pady = 5, fg = MyFg, bg = MyBg)
            MainFrame.place(x = 60, y = 190)#grid(row = 2, column = 0, columnspan = 3)
                        
            tk.Button(MainFrame, text = "--diff", command = lambda: RunCommand("-d", e1.get(), e2.get())).grid(row = 3, column = 0)
            tk.Button(MainFrame, text = "--sync", command = lambda: RunCommand("-s", e1.get(), e2.get())).grid(row = 4, column = 0)
            tk.Button(MainFrame, text = "--update", command = lambda: RunCommand("-u", e1.get(), e2.get())).grid(row = 5, column = 0)

            MainOptions = ["--diff, -d", "--sync, -s", "--update, -u"]
            for i in MainOptions:
                j = MainOptions.index(i)
                tk.Label(MainFrame, text = FindFromFile(i, "source/TEXTDATA"), fg = MyFg, bg = MyBg).grid(row = j+3, column = 1, columnspan= 3)
        if RootExists: MainFrame()

def main():
    global MyBg; global MyFg
    global white; global dark
    white = "#ffffff"; dark = "#282828"; black = "#121212"
    MyBg = dark; MyFg = white
    root = tk.Tk()
    root.title(f"DirSync-GUI v{MyVersion}")
    root.geometry("522x500")
    root.configure(bg = black)
    MyImg = ImageTk.PhotoImage(Image.open("source/Image_dsg.JPG"))
    tk.Label(root, image = MyImg).grid(row = 0, column = 0, columnspan = 3)
    Main(root)
    root.mainloop()
main()