import time
import webbrowser
import ctypes  # An included library with Python install.
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, 0)
Mbox('You have been shreked', 'Your time on earth is ogre', 1)

timeout = time.time() + 3*5   
while True:


    test = 0
    webbrowser.open("https://media.tenor.com/lg0cvDLYL9EAAAAC/get-shrekt-shrek.gif", new=1)
    if test == 5 or time.time() > timeout:
        break
    test = test - 1
