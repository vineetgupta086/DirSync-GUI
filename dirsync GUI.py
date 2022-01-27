# for running shell commands
import subprocess as sp

# for gui
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# for app update
import requests
import webbrowser

global MyFg; global MyBg
with open("VERSION") as v:
    MyVersion = v.readline()

def CheckVersion():
    ProgVersion = requests.get("")

root = tk.Tk()
root.title(f"dirsync GUI v{MyVersion}")
