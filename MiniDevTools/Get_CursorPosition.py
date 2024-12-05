import TerminalFormatting as a
from pyautogui import position as mousePosition
from time import sleep

while True:
    x, y = mousePosition()
    print(f"{a.Red}{a.Bold}  [X: {x}]  [Y: {y}]          {a.Reset}", end="\r")
    sleep(0.04)
