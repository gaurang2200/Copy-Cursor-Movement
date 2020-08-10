"""
Created on Sat Dec 25 19:03:08 2019

@author: Gaurang Gupta
"""

#This program can record your mouse movements once per RunTime
import pyautogui as pag
import tkinter as tki
import time

def move(x, y):
    global j
    global arrNum
    global coordinateX
    global coordinateY
    global clicks
    
    #print("Mouse is at position ({0}, {1})".format(x,y))
    coordinateX[j] = x
    coordinateY[j] = y
    j += 1

    
def click(x, y, button, pressed):
    Button = button
    global j
    #print("Mouse {2} {0} at {1}".format('Pressed' if pressed else 'Released', (x,y), button ))
    
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
    global scrollX, scrollY
    print("Mouse scrolled {0} at {1}".format((dx, dy), (x,y)))
    if dx == 0 :
        scrollX += 1
    elif dx == -1:
        scrollX -= 1
    elif dy == 0 :
        scrollY += 1
    elif dy == -1:
        scrollY -= 1
    


arrSize = 2000
#empty = [0 for k in range(arrSize)]
coordinateX = [0 for row in range(arrSize)]
coordinateY = [0 for col in range(arrSize)]
clicks = [0 for cli in range(arrSize)]
# scrolls = [0 for scr in range(arrSize)]
#
# int(input("Enter the number of seconds: "))
# timeEvent = [0 for t in range(timeout*100)]

j = 0

def Record():
    listen.start()
    print('Recording Started')


def StopRecord():
    listen.stop()
    print('Recording Stopped')
    #print(clicks)

            
def Play() :
    time.sleep(2)
    root.destroy()
    root.mainloop()
    
    global j
    
    i = 4
    pag.moveTo(coordinateX[i], coordinateY[i])
    
    while i < (j-1) :
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
    
    print("Recording Played")
 

#def destroyTimes():
#    times.destroy()


root = tki.Tk()
root.title("Cursor Recording")
root.geometry("500x200+600+300")
root.configure(bg="#0077FB")


label1 = tki.Label(root, text = "This Program records your Mouse Action and then copies it \n", bg="#0077FB", fg="black" ,font="TimesNewRoman 10 bold", pady=5)
label1.grid(row=0, column=0, columnspan=2);

button1 = tki.Button(root, text="Start Recording", bg="white", fg="black", borderwidth=3, relief="groove", font="Consolas 10 bold", pady=5, width=15, command = Record)
button1.grid(row=1, column=0, pady = 5)

button2 = tki.Button(root, text="Stop Recording", bg="white", fg="black", borderwidth=3, relief="groove", font="Consolas 10 bold", pady=5, width=15, command = StopRecord)
button2.grid(row=1, column=1, pady = 5)

hrLine = tki.Label(root, text="---------------------------------------------------------------------------", bg="#0077FB")
hrLine.grid(row=2, column=0, columnspan=2)

label1 = tki.Label(root, text="Play the Recording: ", bg="#0077FB", fg="black" ,font="TimesNewRoman 10 bold", pady=5)
label1.grid(row=3, column=0, columnspan=1);

button3 = tki.Button(root, text="Play", bg="white", fg="black", borderwidth=3, relief="ridge", font="Consolas 10 bold", pady=3, width=15, command = Play)
button3.grid(row=3, column=1, pady = 5, columnspan=1)

root.mainloop()