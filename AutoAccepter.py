import pyautogui
from time import strftime, localtime

r_slash = ']'
l_slash = '['

while(True):
    try:
        button7location = pyautogui.locateOnScreen('lib/accept.png')
        button7location
        buttonx, buttony = pyautogui.center(button7location)
        buttonx, buttony
        pyautogui.click(buttonx, buttony)
        time = strftime("%H:%M:%S", localtime())
        print(l_slash + time + r_slash, '[dota2.exe] - Game Founded, accepting...')
    except:
        pass
