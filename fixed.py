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
    time = 0.01

    x = 0
    print("Press Ctrl + C to stop")
    pyautogui.moveTo(midx, midy, duration = time) # moves mouse to center
    print("Moving mouse to (", midx, ",", midy, ")")
    while(x < 1): 
        pyautogui.dragTo(midx+500, midy, button='left') #moves mouse +500 pixels in x
        print("Moving mouse to (", midx+500, ",", midy, ")")

        pyautogui.dragTo(midx, midy-500, button='left')
        print("Moving mouse to (", midx, ",", midy-500, ")")

        pyautogui.dragTo(midx-500, midy,button='left'  )
        print("Moving mouse to (", midx-500, ",", midy-500, ")")

        pyautogui.dragTo(midx, midy+500,button='left'  )
        print("Moving mouse to (", midx, ",", midy+500, ")")

        pyautogui.dragTo(midx+500, midy,button='left'  )
        print("Moving mouse to (", midx+500, ",", midy, ")")
        


       
        

                




