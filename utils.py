import subprocess

def VersionValue(val):
    """Function for comparing version values

    Args:
        val (string): version number of the program (Eg: 2.3.1)

    Returns:
        int: converts the number to an int (Eg: 2.3.1 becomes 231)
    """
    NewVal = str(val).replace(".","")
    if len(NewVal) == 2:
        return int(str(NewVal+"0"))
    elif len(NewVal) == 3:
        return int(str(NewVal))

def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=False)
    return completed

def FindFromFile(s, file):
    TextData = open(file).readlines()
    
    for Line in TextData:  
        if Line.startswith(s):
            return Line[len(s)+1:len(Line)].strip()

def FindInText(s, text):
    Line = text[text.find(s):len(text)]
    Line = Line[len(s)+1:len(Line)]
    Line = Line[0:Line.find("\n")]
    return Line.strip() #added 1 for colon

def RunCommand(s: str, source: str, target: str):
    run(f"dirsync {source} {target} {s}")