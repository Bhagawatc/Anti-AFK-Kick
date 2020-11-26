import pyautogui 
import pickle
import os
from os import path

if(path.exists("data.dat") == False ):
    resx, resy= pyautogui.size()
    res = "(,", resx, ",", resy, ")"
    midx = int(resx)/2
    midy = int(resy)/2
    display_info = [res, resx, resy, int(midx), int(midy)]
    pickle.dump(display_info, open("data.dat", "wb"))

if(path.exists("data.dat") == True):
    display_info = pickle.load(open("data.dat", "rb"))
    resx = display_info[1]
    resy = display_info[2]
    midx = float(display_info[3])
    midy = float(display_info[4])

    x = 0
    print("Press Ctrl + C to stop")
    while(x < 1): 
        pyautogui.moveTo(midx, midy, duration = 1)
        print("Moving mouse to (", midx, ",", midy, ")")
        pyautogui.moveTo(midx, midy+100, duration = 1)
        print("Moving mouse to (", midx, ",", midy+100, ")")
                




