from tkinter import *
from PIL import Image, ImageTk
import os
import sys
# Create Tkinter Object
root = Tk()




root.title("give em hell")
root.geometry('1000x1000')
# Set geometry(widthxheight)
# arranging application parameters

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)




lbl = Label(root, text = "Current verion bugs, can only use each function once per opening the application")
lbl.grid(row=10)
 
lbl = Label(root, text = "any banishments are on you not me hugs and kisses -(ImNotAlex#4768)")
lbl.grid(row=11)

 
# function to display text when
# button is clicked
def clicked():
    import random as randy
    import pyautogui as gui
    import pyperclip as pc
    import time


    amount = gui.prompt(text='how many times?', title='funny spam bot' , default=69)
    num2 = int(amount)

    loop = 0
    gui.alert(text='prepare yourself you have 5 secodnds to click the text bar for discord', title='', button='im prepared')
    time.sleep(5)
    while loop <= num2:
        if num2 > 10:
            time.sleep(1)
        number = randy.randint(0, 10000)
        pc.copy(number)
        paste = pc.paste()
        print(paste)
        gui.hotkey('command', 'v')
        gui.hotkey('enter')
        print(loop)
        loop = loop + 1
        
 
# button widget with red color text
# inside
btn = Button(root, text = "Number Spam" , fg = "black", command=clicked)
# set Button grid
btn.grid(column=0, row=0)

def clicked2():
    import pyautogui as gui
    import pyperclip as pc
    import time


    amount = gui.prompt(text='how many times?', title='funny spam bot' , default=69)
    num2 = int(amount)

    loop = 0
    gui.alert(text='prepare yourself you have 5 secodnds to click the text bar for discord', title='', button='im prepared')
    time.sleep(5)
    while loop <= num2:
        if num2 > 10:
            time.sleep(1)
        number = 'https://cdn.discordapp.com/attachments/933201726905937960/933485189886271578/funny.png'
        pc.copy(number)
        paste = pc.paste()
        print(paste)
        gui.hotkey('command', 'v')
        gui.hotkey('enter')
        print(loop)
        loop = loop + 1


btn = Button(root, text = "Image Spam" , fg = "black", command=clicked2)
# set Button grid
btn.grid(column=0, row=2)

def clicked3():
    import pyautogui as gui
    import pyperclip as pc
    import time


    amount = gui.prompt(text='how many times?', title='funny spam bot' , default=69)
    num2 = int(amount)

    loop = 0
    gui.alert(text='prepare yourself you have 5 secodnds to click the text bar for discord', title='', button='im prepared')
    time.sleep(5)
    while loop <= num2:
        if num2 > 10:
            time.sleep(1)
        number = '@everyone'
        pc.copy(number)
        paste = pc.paste()
        print(paste)
        gui.hotkey('command', 'v')
        gui.hotkey('enter')
        print(loop)
        loop = loop + 1
    


btn = Button(root, text = "@everyone spam" , fg = "black", command=clicked3)
# set Button grid
btn.grid(column=0, row=3)




root.mainloop()