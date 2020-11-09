import pyautogui, time, sys, keyboard, winsound, pydirectinput


def playBeep(fre,dur):
    winsound.Beep(fre,dur) 

def mineForward(sleepfor):
    pyautogui.mouseDown()
    pydirectinput.keyDown("w")
    time.sleep(sleepfor)
    pyautogui.mouseUp()
    pydirectinput.keyUp("w")

def turnRight():
    pydirectinput.move(600,None)

def turnLeft():
    pydirectinput.move(-600,None)

def setFace():
    pydirectinput.press("t")
    f = open("lookCommand.txt", 'r')
    for word in f:
        pyautogui.typewrite(word)
    pydirectinput.press("enter")


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

setFace()

pydirectinput.move(2400,None)

for x in range(0,8):
    mineForward(5.8)
    turnRight()
    mineForward(.20)
    turnRight()
    mineForward(5.8)
    turnLeft()
    mineForward(.20)
    turnLeft()
    if keyboard.is_pressed(' '):
        break


time.sleep(1)

playBeep(500,100 )