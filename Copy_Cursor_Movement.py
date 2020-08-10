import pyautogui as pag
from pynput import mouse
import time


def move(x, y):
    global j 
    print("Mouse is at position ({0}, {1})".format(x,y))
    coordinateX[j] = x
    coordinateY[j] = y
    j += 1
    
    
def click(x, y, button, pressed):
    Button = button
    global j
    print("Mouse {2} {0} at {1}".format('Pressed' if pressed else 'Released', (x,y), button ))
    
    #'''
    if pressed :
        if button == Button.left:
            clicks[j] = 1
        elif button == Button.right:
            clicks[j] = 2
        elif button == Button.middle:
            clicks[j] = 3

    else :
        clicks[j] = 10

    coordinateX[j] = x
    coordinateY[j] = y
    j += 1

    
def scroll(x, y, dx, dy):
    print("Mouse scrolled {0} at {1}".format('Down' if dy<0 else 'Up', (x,y)))

#scrolls = [0 for scr in range(arrSize)]

#'''
timeout = int(input("Enter the number of seconds: "))

arrSize = timeout*70

coordinateX = [0 for row in range(arrSize)]
coordinateY = [0 for col in range(arrSize)]
clicks = [0 for cli in range(arrSize)]
#timeEvent = [0 for t in range(timeout*100)]

j = 0
listen = mouse.Listener(on_move=move, on_click= click, on_scroll=scroll)

listen.start()
time.sleep(timeout)
listen.stop()


#'''
i = 0
#print(coordinateX, clicks)
pag.moveTo(coordinateX[i], coordinateY[i], duration=2)
while i < j :
    pag.moveTo(coordinateX[i], coordinateY[i])
    
    if clicks[i] == 1 :
        pag.mouseDown(button='left')
        #pag.click()
        i += 1
        while clicks[i] == 0 :
            pag.moveTo(coordinateX[i], coordinateY[i])
            i += 1
        pag.mouseUp(button='left')
        
    if clicks[i] == 2 :
        pag.mouseDown(button='right')
        i += 1
        while clicks[i] == 0 :
            pag.moveTo(coordinateX[i], coordinateY[i])
            i += 1
        pag.mouseUp(button='right')
    
    if clicks[i] == 3 :
        pag.mouseDown(button='middle')
        i += 1
        while clicks[i] == 0 :
            pag.moveTo(coordinateX[i], coordinateY[i])
            i += 1
        pag.mouseUp(button='middle')
      
    i += 1
    #time.sleep(0.001)
        
#'''