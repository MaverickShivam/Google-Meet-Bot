import webbrowser
import keyboard
import time
import numpy as np
from PIL import ImageGrab as ig
import cv2
import pyautogui
import pytesseract
import re
from gtts import gTTS
import os
from playsound import playsound
pytesseract.pytesseract.tesseract_cmd=r"E:\tesseract-4.0.0-alpha\tesseract.exe"
def pressbutton(key):
    keyboard.press(key)
    time.sleep(0.2)
    keyboard.release(key)
    time.sleep(0.2)
def mouseclick(xpos,ypos,wpos,hpos):
    pyautogui.click(int(xpos+wpos/2)+200, int(ypos+hpos/2)+500)
def process_img(original_image):
    processed_img=cv2.cvtColor(original_image,cv2.COLOR_RGB2GRAY)
    #resize image
    #processed_img = cv2.resize(processed_img, dim, interpolation = cv2.INTER_AREA)
    #processed_img=cv2.Canny(processed_img,threshold1=200,threshold2=300)
    #print(pyautogui.position())
    #processed_img=cv2.circle(processed_img, pyautogui.position(), 5, (255,0,0), thickness=1, lineType=8, shift=0)
    return processed_img
#win32gui.GetCursorPos(point)   
#1920 1080


#myobj=gTTS("yes mam",lang="en",slow=False)
#myobj.save("yesmam.mp3")

webbrowser.open("https://meet.google.com/dyp-xppt-biv"+"?authuser=1")
time.sleep(10)
for i in range(0,4):
    pressbutton("tab")
    time.sleep(0.2)

time.sleep(1)

pressbutton("enter")
pressbutton("tab")
pressbutton("enter")
lasttime=int(time.time())-60
joined=False
caption=False
while(True):
    screen=np.array(ig.grab(bbox=(200,500,910,1020)))
    screen=cv2.cvtColor(screen,cv2.COLOR_BGR2RGB)
    new_screen=process_img(screen)
    ret, thresh1 = cv2.threshold(new_screen, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    #thresh2=cv2.adaptiveThreshold(new_screen,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
    #cv2.imshow("threshold",thresh1)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,  
                                                 cv2.CHAIN_APPROX_NONE) 
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        rect = cv2.rectangle(screen, (x, y), (x + w, y + h), (0, 255, 0), 2) 
        cropped = new_screen[y:y + h, x:x + w]
        textonscreen=str(pytesseract.image_to_string(cropped)).strip()
        if(textonscreen=="Join now"):
            mouseclick(x,y,w,h)
            time.sleep(5)
            joined=True
        if(not caption and textonscreen=="Turn on capnons"):
            mouseclick(x,y,w,h)
            pyautogui.moveTo(5, 5, duration = 1) 
            caption=True
            time.sleep(5)
        #if(caption and textonscreen=="Turn off captions"):
            #pyautogui.moveTo(420, 450, duration = 0.5)
            #time.sleep(0.5)
            #pyautogui.moveTo(5, 5, duration = 0.5) 
        if(joined and textonscreen.find("Shivam")>0 ):
            print("worked-------")
            if(lasttime+60 < int(time.time())):  
                pyautogui.moveTo(60,970 ,duration = 0.5) 
                pyautogui.click(60, 970)
                playsound("yesmam.mp3")
                pyautogui.click(60, 970)
                pyautogui.moveTo(5, 5, duration = 0.5)
                time.sleep(5)
                lasttime=int(time.time())
            elif(int(time.time())> lasttime+10): 
                pyautogui.click(810, 120)
                time.sleep(1)
                keyboard.write("yes mam")
                time.sleep(1)
                pressbutton("enter")
                time.sleep(1)
                pyautogui.click(920, 140)
                time.sleep(1)
                pyautogui.moveTo(5, 5, duration = 0.5)
                time.sleep(7)
            continue
        print(textonscreen)    
    cv2.imshow("window",rect)
    if(cv2.waitKey(25) & 0xFF ==ord('q')):
        cv2.destroyAllWindows()
        break
    
