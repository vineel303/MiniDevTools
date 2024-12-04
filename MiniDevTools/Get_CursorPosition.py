from pyautogui import position as mousePosition
from time import sleep
import TerminalFormatting as a

while True:
    x, y = mousePosition()
    print(f"{a.Red}{a.Bold}  [X: {x}]  [Y: {y}]          {a.Reset}", end="\r")
    sleep(0.04)
