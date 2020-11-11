import pyautogui #use pip install pyautogui in your terminal
import os
import datetime
import sys

print("press ctrl + C to quit.")

meetid = input("ID:  \n")
meetpsd = input("Password:  \n")
meeth = int(input("Hour of meeting: \n"))
meetm = int(input("Minute of meeting: \n"))
amPm1 = input("Am or Pm: \n")

alarmH = meeth
alarmM = meetm
amPm = amPm1
print("Waiting for class",alarmH,alarmM,amPm)
if (amPm == "pm"):
        alarmH = alarmH + 12
while(1 == 1):
    if(alarmH == datetime.datetime.now().hour and
        alarmM == datetime.datetime.now().minute) :
        print("Time for class")
   
        try:
            pyautogui.PAUSE = 5
            pyautogui.press('win')
            pyautogui.PAUSE = 5
            pyautogui.write('zoom', interval=0.05)
            pyautogui.PAUSE = 4

            pyautogui.press('Enter')
            pyautogui.PAUSE = 
            pyautogui.moveTo(536, 286)
            pyautogui.getWindowsWithTitle("Zoom")[0].maximize()
            pyautogui.PAUSE = 8
            pyautogui.click(button='left')
            pyautogui.write(meetid, interval=0.05)
            pyautogui.PAUSE = 12
            pyautogui.press('Enter')
            pyautogui.typewrite(meetpsd, interval=0.05)
            pyautogui.press('Enter')

        except KeyboardInterrupt:
            print("\nDone")
