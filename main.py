from this import d
import pyautogui
import time
import random
import cv2 as cv
import numpy as np

DELAY_BETWEEN_COMMANDS = random.uniform(0,2)
def main():

    # Initialized pyautogui
    pyautogui.FAILSAFE = True


    print("Starting", end="")
    #countdown timer
    print("Starting", end="")
    for i in range(0, 10):
        print(".", end="")
        time.sleep(1)
    print("Go")

    #Do anything
    #reportMousePosition()
    portalSearch()
    #pyautogui.displayMousePosition()
    '''number = 0
    while number < 30:
        clickOnChaos()
        moveInChaos1()
        moveInChaos2() 
        moveInChaos3()
        moveInChaos4()
        leaveChaos() 
        number = number+1
        if number % 10 == 0:
            repairEquip()'''
    #done
    print("Done")

def reportMousePosition(seconds=10):
    for i in range(0, seconds):
        print(pyautogui.position())
        time.sleep(1)

def clickOnChaos():   
    i = random.randrange(1, 2)
    xcord = random.uniform(1117, 1395)
    ycord = random.uniform(352, 564)
    #coord is 1080, 406
    pyautogui.moveTo(xcord, ycord, i)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click(button='right')
    xcord = random.uniform(1403, 1676)
    ycord = random.uniform(839, 875)
    #coord is 1435, 825
    pyautogui.moveTo(xcord, ycord, i)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()
    xcord = random.uniform(859, 956)
    ycord = random.uniform(589, 608)
    pyautogui.moveTo(xcord, ycord, i)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()
    time.sleep(10)

def moveInChaos1():
    i = random.randrange(1, 2)
    xcord = random.uniform(270, 1236)
    ycord = random.uniform(114, 942)
    pyautogui.moveTo(xcord, ycord, i)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click(button='right')
    time.sleep(4)
    pyautogui.keyDown('r')
    pyautogui.keyUp('r')
    time.sleep(0.20)
    pyautogui.keyDown('f')
    pyautogui.keyUp('f')
    time.sleep(0.50)
    pyautogui.keyDown('e')
    time.sleep(0.25)
    pyautogui.keyUp('e')
    time.sleep(0.2)
    xcord = random.uniform(270, 1236)
    ycord = random.uniform(114, 942)
    pyautogui.moveTo(xcord, ycord, i)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()
    pyautogui.keyDown('w')
    time.sleep(0.50)
    pyautogui.keyUp('w')
    time.sleep(0.50)
    xcord = random.uniform(270, 1236)
    ycord = random.uniform(114, 942)
    pyautogui.moveTo(xcord, ycord, i)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()
    pyautogui.keyDown('q')
    time.sleep(0.50)
    pyautogui.keyUp('q')
    time.sleep(4)
    pyautogui.keyDown('d')
    time.sleep(4)
    pyautogui.keyUp('d')

def moveInChaos2():
    i = random.randrange(1, 2)
    xcord = random.uniform(270, 1236)
    ycord = random.uniform(114, 942)
    pyautogui.moveTo(xcord, ycord, i)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click(button='right')
    time.sleep(0.2)
    pyautogui.keyDown('r')
    pyautogui.keyUp('r')
    time.sleep(0.3)
    xcord = random.uniform(270, 1236)
    ycord = random.uniform(114, 942)
    pyautogui.moveTo(xcord, ycord, i)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()
    pyautogui.keyDown('e')
    time.sleep(0.30)
    pyautogui.keyUp('e')
    time.sleep(0.25)
    pyautogui.keyDown('w')
    time.sleep(0.30)
    pyautogui.keyUp('w')
    time.sleep(0.40)
    xcord = random.uniform(270, 1236)
    ycord = random.uniform(114, 942)
    pyautogui.moveTo(xcord, ycord, i)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()
    pyautogui.keyDown('q')
    time.sleep(0.50)
    pyautogui.keyUp('q')
    time.sleep(4)
    pyautogui.keyDown('d')
    time.sleep(4)
    pyautogui.keyUp('d')

def moveInChaos3():
    i = random.randrange(1, 2)
    xcord = random.uniform(270, 1236)
    ycord = random.uniform(114, 942)
    pyautogui.moveTo(xcord, ycord, i)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click(button='right')
    time.sleep(0.60)
    pyautogui.keyDown('r')
    pyautogui.keyUp('r')
    time.sleep(0.70)
    pyautogui.keyDown('f')
    pyautogui.keyUp('f')
    time.sleep(0.3)
    xcord = random.uniform(270, 1236)
    ycord = random.uniform(114, 942)
    pyautogui.moveTo(xcord, ycord, i)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()
    pyautogui.keyDown('e')
    time.sleep(0.50)
    pyautogui.keyUp('e')
    time.sleep(0.40)
    pyautogui.keyDown('w')
    time.sleep(0.50)
    pyautogui.keyUp('w')
    time.sleep(0.20)
    xcord = random.uniform(270, 1236)
    ycord = random.uniform(114, 942)
    pyautogui.moveTo(xcord, ycord, i)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()
    pyautogui.keyDown('q')
    time.sleep(0.50)
    pyautogui.keyUp('q')
    time.sleep(4)
    pyautogui.keyDown('d')
    time.sleep(4)
    pyautogui.keyUp('d')

def moveInChaos4():
    i = random.randrange(1, 2)
    xcord = random.uniform(270, 1236)
    ycord = random.uniform(114, 942)
    pyautogui.moveTo(xcord, ycord, i)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.keyDown('r')
    pyautogui.keyUp('r')
    xcord = random.uniform(270, 1236)
    ycord = random.uniform(114, 942)
    pyautogui.moveTo(xcord, ycord, i)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()
    time.sleep(0.7)
    pyautogui.keyDown('e')
    time.sleep(0.50)
    pyautogui.keyUp('e')
    time.sleep(0.60)
    pyautogui.keyDown('w')
    time.sleep(0.50)
    pyautogui.keyUp('w')
    time.sleep(1)
    pyautogui.keyDown('q')
    time.sleep(0.50)
    pyautogui.keyUp('q')
    time.sleep(4)
    xcord = random.uniform(270, 1236)
    ycord = random.uniform(114, 942)
    pyautogui.moveTo(xcord, ycord, i)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()
    pyautogui.keyDown('d')
    time.sleep(4)
    pyautogui.keyUp('d')

# use for both x axis 
def randomCoord(defaultPixel, maxOffset):
    # randomize an x or y coord plus or minus
    # use python's random 
    return random.randint(defaultPixel - maxOffset, defaultPixel + maxOffset)

def leaveChaos():
    i = random.randrange(1, 2)
    xcord = random.uniform(74, 194)
    ycord = random.uniform(266, 300)
    #leave coord 288, 354
    pyautogui.moveTo(xcord, ycord, i)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()
    xcord = random.uniform(858, 952)
    ycord = random.uniform(578, 586)
    pyautogui.moveTo(xcord, ycord, i)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()
    time.sleep(10)
#coordinate for Leave = 288, 354
def repairEquip():
    pyautogui.keyDown('Alt')
    pyautogui.keyDown('p')
    time.sleep(1)
    pyautogui.keyUp('p')
    pyautogui.keyUp('Alt')
    i = random.randrange(1,2)
    xcord = random.uniform(1242, 1267)
    ycord = random.uniform(679, 702)
    pyautogui.moveTo(xcord, ycord, i)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()
    xcord = random.uniform(1006, 1174)
    ycord = random.uniform(414, 444)
    pyautogui.moveTo(xcord, ycord, i)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()
    xcord = random.uniform(1724, 1861)
    ycord = random.uniform(1004, 1048)
    pyautogui.moveTo(xcord, ycord, i)
    time.sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()
    pyautogui.keyDown('Esc')
    time.sleep(1)
    pyautogui.keyUp('Esc')

def portalSearch():
    x = 0
    y = 0
    i = random.randrange(1, 2)
    im = pyautogui.screenshot(region=(1596,40, 294, 256))
    width, height = im.size
    if pyautogui.locateOnScreen('portal.jpg', confidence=0.8) != None:
        x, y = pyautogui.locateOnScreen('portal.jpg', confidence=0.8)
        x = ((x - 1742)* 4 + 960)
        y = ((y - 168)*4 + 540)
        pyautogui.sleep(1)
        pyautogui.moveTo(x, y, i)
        pyautogui.sleep(DELAY_BETWEEN_COMMANDS)
        pyautogui.click(button= 'right')
    else:
        exit

if __name__ == "__main__":
    main()