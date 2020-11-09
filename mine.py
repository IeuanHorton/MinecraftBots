import pyautogui, time, sys, keyboard, winsound


def playBeep(fre,dur):
    winsound.Beep(fre,dur) 

print("Starting in 5 seconds")
time.sleep(1)
print("4")
time.sleep(1)

playBeep(1000,250)

print("3")
time.sleep(1)

playBeep(1000,200)

print("2")
time.sleep(1)

playBeep(1000,150 )

print("1")
time.sleep(1)

playBeep(1250,100 )


pyautogui.mouseDown()
while 1:
        if keyboard.is_pressed(' '):
            break
pyautogui.mouseUp()

playBeep(500,100 )


