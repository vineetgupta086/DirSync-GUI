# for running shell commands
import subprocess as sp
import os

# for gui
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

# for app update
import requests
import webbrowser
import utils

# global MyBg; global MyFg
with open("VERSION") as v:
    MyVersion = v.readline()

class Main:
    global RootExists
    RootExists = True
    def __init__(self, parent):
        def UpdateVersion():
            """Compares the current version and latest version of the program.
            """
            ProgVersion = requests.get("https://raw.githubusercontent.com/vineetgupta086/DirSync-GUI/main/VERSION").text
            if utils.VersionValue(MyVersion) < utils.VersionValue(ProgVersion):
                # update needed
                # MyMsg = f"DirSync-GUI v{ProgVersion} available. Do you want to update?\nClick 'Yes' to go the repository for latest version."
                MyMsg = f"DirSync-GUI v{ProgVersion} available. Do you want to update?\nClick 'Yes' if you have Git installed and want to clone the repository for latest version."
                response = messagebox.askquestion(title = f"DirSync-GUI v{MyVersion}", message = MyMsg)
                if response == "no":
                    pass
                elif response == "yes":
                    try:
                        # download msi file
                        # webbrowser.open("https://github.com/vineetgupta086/DirSync-GUI")
                        utils.run("git clone https://github.com/vineetgupta086/DirSync-GUI")
                        RootExists = False
                        parent.destroy()
                    except Exception as e:
                        messagebox.showerror("Software update", "An error occured during the update: {e}")
            elif int(utils.VersionValue(MyVersion)) == int(utils.VersionValue(ProgVersion)):
                messagebox.showinfo(f"DirSync-GUI v{MyVersion}", "You are currently using the latest version.")
            tk.Button(parent, text = "Check for updates", fg = white, bg = dark, command = UpdateVersion, padx = 5).place(x = 405, y = 92)#grid(row = 1, column = 2, columnspan = 1)
        UpdateVersion()
        # self.MainOptions()

        def MainFrame():
            MainFrame = tk.LabelFrame(parent, text = "Main Options", padx = 5, pady = 5, fg = MyFg, bg = MyBg)
            MainFrame.place(x = 10, y = 120)#grid(row = 2, column = 0, columnspan = 3)
            tk.Label(MainFrame, fg = MyFg, bg = MyBg, text = "Source Directory:  ").grid(row = 0, column = 0)
            SourceDir = tk.Entry(MainFrame, fg = MyFg, bg = MyBg, width = 53)
            SourceDir.grid(row = 0, column = 1, columnspan = 1)
            tk.Label(MainFrame, text = " "*3, fg = MyFg, bg = MyBg).grid(row = 0, column = 2, columnspan = 1)
            tk.Button(MainFrame, text = "Browse").grid(row = 0, column = 3, columnspan= 1)
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