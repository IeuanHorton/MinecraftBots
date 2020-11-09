import pydirectinput, time, sys, keyboard, winsound, pyautogui
from multiprocessing import Process

def playBeep(fre,dur):
    winsound.Beep(fre,dur) 

def tower():
    while 1:
        pydirectinput.rightClick()
        pydirectinput.keyDown("space")
        

def switchdown():
    inventory = "1"
    pydirectinput.keyDown(inventory)
    while 1: 
        time.sleep(32)
        inventory = changeInvetory(inventory)
        pydirectinput.keyDown(inventory)
        playBeep(1250,100 )

def changeInvetory(slot):
    if(slot == "1"):
        return "2"
    if(slot == "2"):
        return "3"
    if(slot == "3"):
        return "4" 
    if(slot == "4"):
        return "5"
    if(slot == "5"):
        return "6"
    if(slot == "6"):
        return "7" 
    if(slot == "7"):
        return "8"
    if(slot == "8"):
        return "9"
    if(slot == "9"):
        return "1"

if __name__ == "__main__":

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

    t1 = Process(target = tower)
    t2 = Process(target = switchdown)

    t1.start()
    t2.start()

    while 1:
        if keyboard.is_pressed('p'):
            playBeep(500,100)
            t1.terminate()
            t2.terminate()
            break