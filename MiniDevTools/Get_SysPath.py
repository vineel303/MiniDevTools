import vinTerminalFormatting as a
import sys

def sysPath():
    a.specialPrint("Items in sys.path:", a.Dim)
    sysPath = sys.path
    for i in sysPath:
        print(f"{a.Dim}{sysPath.index(i)}: {a.Reset}{a.Yellow}{i}{a.Reset}")
