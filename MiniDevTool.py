import vinTerminalFormatting as a
import subprocess

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
"""
HOW TO ADD NEW FUNCTIONS?
1. ::: Total_Number_Of_Integers += 1
2. Add to printStatement (on the last line)::: < int >: < file name >
3. Add:::
    3(1)A. Add::: import MiniDevTools.< file name > as < alias >
    3(1)B. Add to "def RUN(value):":::
        ""
        if value == < int >:
            < alias >.< function >
            p()
        ""
OR Add:::
    3(2)A. Add to "def RUN(value):":::
        ""
        if value == < int >:
            runInNewWindow("< relative file path >")
        ""
"""
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

# import from MiniDevTools folder
import MiniDevTools.Get_SysPath as a1

# the PRINT STATEMENTS
Total_Number_Of_Integers = 2
printStatement = """0: Get sys.path
1: Get Cursor position"""

# the PRIMARY FUNCTIONS
def runInNewWindow(value):
    subprocess.Popen(["python", value], creationflags=subprocess.CREATE_NEW_CONSOLE)

def RUN(value):
    if value == 0:
        a1.sysPath()
        p()
    if value == 1:
        runInNewWindow(r"MiniDevTools\Get_CursorPosition.py")

### --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
### --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
## static code

#secondary functions
def p():
    print("")

def getUserInput(printValue):
    global printStatement
    global Total_Number_Of_Integers
    if printValue:
        a.specialPrint("List: ", a.Dim)
        a.specialPrint(printStatement, a.Magenta + a.Bold)
    try:
        userInput = int(a.specialInput("Input: ", a.Dim, a.Cyan + a.Bold))
        if userInput >= Total_Number_Of_Integers:
            print("Invalid input value. Retry.")
            return getUserInput(0)
    except:
        print("Invalid input type. Retry.")
        return getUserInput(0)
    return userInput

#variables
printAtBreak = "--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---"

#main function
if __name__ == "__main__":
    while True:
        userInput = getUserInput(1)
        p() #universal blank line
        RUN(userInput)
        a.specialPrint(printAtBreak, a.Bold + a.Magenta)
        a.specialPrint(printAtBreak, a.Bold + a.Cyan)
        p() #universal blank line
