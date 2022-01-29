from tkinter import messagebox
import requests
import utils

def UpdateVersion(root = None):
    """Compares the current version and latest version of the program.
    """
    RootExists = True
    ProgVersion = utils.FindInText("VERSION",requests.get("https://raw.githubusercontent.com/vineetgupta086/DirSync-GUI/main/source/TEXTDATA").text)

    try:
        MyVersion = utils.FindFromFile("VERSION", "source/TEXTDATA")
    except Exception as e:
        MyVersion = "0.0"
        response = messagebox.askokcancel("Software installation", f"DirSync v{ProgVersion} available. Click 'OK' to continue.")
        if response == "ok":
            print(f"Installing DirSync v{ProgVersion}")
        elif response == "cancel":
            pass
    # print(f"{MyVersion} & {ProgVersion}")
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
                if not root == None: root.destroy()
            except Exception as e:
                messagebox.showerror("Software update", "An error occured during the update: {e}")
    elif int(utils.VersionValue(MyVersion)) == int(utils.VersionValue(ProgVersion)):
        messagebox.showinfo(f"DirSync-GUI v{MyVersion}", "You are currently using the latest version.")
        RootExists = True
    elif int(utils.VersionValue(MyVersion)) > int(utils.VersionValue(ProgVersion)):
        messagebox.showwarning(f"DirSync-GUI v{MyVersion}", f"Your version is {MyVersion} but the latest version is {ProgVersion}. Try Again later.")
        RootExists = True
        # messagebox.showinfo(f"DirSync-GUI v{MyVersion}", f"Your version is {MyVersion} but the latest version is {ProgVersion}. Try Again later.")

    return RootExists