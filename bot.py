import webbrowser
import keyboard
import time
webbrowser.open("https://meet.google.com/vzb-uqge-inm"+"?authuser=1")
time.sleep(3)
def pressbutton(key):
    keyboard.press(key)
    time.sleep(0.2)
    keyboard.release(key)
    time.sleep(0.2)


for i in range(0,3):
    pressbutton("tab")

time.sleep(1)

pressbutton("enter")
pressbutton("tab")
pressbutton("enter")

for i in range(0,3):
    pressbutton("tab")

pressbutton("enter")

