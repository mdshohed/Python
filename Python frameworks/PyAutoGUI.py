#auto message: 


import pyautogui
import time

i = 10
while i>0:
    time.sleep(1)
    pyautogui.typewrite("Hello")
    time.sleep(1)
    pyautogui.press("enter")
    i = i-1
    
    

[Install Link:](https://pypi.org/project/PyAutoGUI)
