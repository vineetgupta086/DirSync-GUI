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