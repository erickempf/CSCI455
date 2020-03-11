import tkinter as tk
import time
from Maestro import Controller

#Jalen Comment here
##-------------BEGIN GUI CLASS--------------------------------------

MOTORS = 0
TURNING = 1
BODY = 2
HEAD_TURN = 3
HEAD_TILT = 4


class myGUI():
    def __init__(self,win):

        self.commandList = []
        self.tango = Controller()
        self.body = 6000
        self.headTurn = 6000
        self. headTilt = 6000
        self.motors = 6000
        self.turn = 6000
        
        self.win = win
        self.win.geometry("800x410")
        self.size = 50
        
        self.order = [[100,150,""],[175,225,""],[250,300,""],[325,375,""],[400,450,""],[475,525,""],[550,600,""],[625,675,""]]

        self.movex = 5
        self.movey = 5

        self.turnx = 5
        self.turny = 5 + self.size
        
        self.headtiltx = 5  
        self.headtilty = 5 + 2*self.size

        self.headturnx = 5  
        self.headturny = 5 + 3*self.size
        
        self.bodyx = 5  
        self.bodyy = 5 + 4*self.size

        self.playx = 5
        self.playy = 405 - 2* self.size

        self.trashx = 5  
        self.trashy = 405 - self.size
        self.count=0

    def controls(self):
        self.controls = tk.Canvas(win,bd = "0", bg="black", width=self.size+5, height="410")
        self.controls.create_rectangle(5,5,self.size,self.size,fill="red",outline="white")                     #MOVE
        self.controls.create_rectangle(5,5+self.size,self.size,2*self.size,fill="blue",outline="white")       #LEFT/RIGHT
        self.controls.create_rectangle(5,5+2*self.size,self.size,3*self.size,fill="yellow",outline="white") #LOOK UP/DOWN
        self.controls.create_rectangle(5,5+3*self.size,self.size,4*self.size,fill="green",outline="white")   #LOOK LEFT/RIGHT
        self.controls.create_rectangle(5,5+4*self.size,self.size,5*self.size,fill="pink",outline="white")     #BODY LEFT/RIGHT

        self.controls.create_rectangle(5,405-self.size,self.size,405,fill="orange",outline="white")         #TRASH
        self.controls.create_rectangle(5,405-2*self.size,self.size,405-self.size,fill="purple",outline="white") #PLAY
        self.controls.bind('<Motion>',self.motion)
        self.controls.pack(side=tk.LEFT)

    def action(self,event):
        print(event.x)
        print(event.y)
        if event.x >= self.movex and event.x < self.movex+self.size and event.y>= self.movey and event.y<self.movey+self.size:
            print("MOVE")
            self.commandList.append(0)
            print(self.commandList)
            self.order[self.count][2] = "red"
            self.console.create_rectangle(self.order[self.count][0],125,self.order[self.count][1],250,outline="Black",fill=self.order[self.count][2])
            self.count = self.count + 1
            self.console.pack(side=tk.LEFT)
        if event.x >= self.turnx and event.x < self.turnx+self.size and event.y>= self.turny and event.y<self.turny+self.size:
            print("TURN")
            self.commandList.append(1)
            self.order[self.count][2] = "blue"
            self.console.create_rectangle(self.order[self.count][0],125,self.order[self.count][1],250,outline="Black",fill=self.order[self.count][2])
            self.count = self.count + 1
            self.console.pack(side=tk.LEFT)
        if event.x >= self.headtiltx and event.x < self.headtiltx+self.size and event.y>= self.headtilty and event.y<self.headtilty+self.size:
            print("TILT HEAD")
            self.commandList.append(2)
            self.order[self.count][2] = "yellow"
            self.console.create_rectangle(self.order[self.count][0],125,self.order[self.count][1],250,outline="Black",fill=self.order[self.count][2])
            self.count = self.count + 1
            self.console.pack(side=tk.LEFT)
        if event.x >= self.headturnx and event.x < self.headturnx+self.size and event.y>= self.headturny and event.y<self.headturny+self.size:
            print("TURN HEAD")
            self.commandList.append(3)
            self.order[self.count][2] = "green"
            self.console.create_rectangle(self.order[self.count][0],125,self.order[self.count][1],250,outline="Black",fill=self.order[self.count][2])
            self.count = self.count + 1
            self.console.pack(side=tk.LEFT)
        if event.x >= self.bodyx and event.x < self.bodyx+self.size and event.y>= self.bodyy and event.y<self.bodyy+self.size:
            print("BODY")
            self.commandList.append(4)
            self.execute(self.commandList)
            self.order[self.count][2] = "pink"
            self.console.create_rectangle(self.order[self.count][0],125,self.order[self.count][1],250,outline="Black",fill=self.order[self.count][2])
            self.count = self.count + 1
            self.console.pack(side=tk.LEFT)
        if self.count == 7 or self.count == 8:
            self.count = 7
        if self.count == -1:
            self.count = 0
        if event.x >= self.trashx and event.x < self.trashx+self.size and event.y>= self.trashy and event.y<self.trashy+self.size:
            print("TRASH")
            print(self.count)
            if self.count == 7:
                self.count = 7
                self.order[self.count][2] = "grey"
                self.console.create_rectangle(self.order[7][0],125,self.order[7][1],250,outline="Black",fill=self.order[7][2])
                self.count = self.count - 1
            elif self.count == 0:
                self.count = 0
                self.order[self.count][2] = "grey"
                self.console.create_rectangle(self.order[self.count][0],125,self.order[self.count][1],250,outline="Black",fill=self.order[0][2])
            else:
                self.order[self.count][2] = "grey"
                self.console.create_rectangle(self.order[self.count][0],125,self.order[self.count][1],250,outline="Black",fill=self.order[self.count][2])
                self.count = self.count - 1
        if event.x >= self.playx and event.x < self.playx+self.size and event.y >= self.playy and event.y < self.playy+self.size:
            self.execute(self.commandList)
            print("stuff2")


        self.console.pack(side=tk.LEFT)

    def console(self):
        self.console = tk.Canvas(win, bd = "0", bg="grey", width= 800-(5+self.size),height = "410")
        self.console.bind('<Motion>',self.motion)
        
        self.console.create_rectangle(self.order[0][0],125,self.order[0][1],250,outline="Black",fill=self.order[0][2])
        self.console.create_rectangle(self.order[1][0],125,self.order[1][1],250,outline="Black",fill=self.order[1][2])
        self.console.create_rectangle(self.order[2][0],125,self.order[2][1],250,outline="Black",fill=self.order[2][2])
        self.console.create_rectangle(self.order[3][0],125,self.order[3][1],250,outline="Black",fill=self.order[3][2])
        
        self.console.create_rectangle(self.order[4][0],125,self.order[4][1],250,outline="Black",fill=self.order[4][2])
        self.console.create_rectangle(self.order[5][0],125,self.order[5][1],250,outline="Black",fill=self.order[5][2])
        self.console.create_rectangle(self.order[6][0],125,self.order[6][1],250,outline="Black",fill=self.order[6][2])
        self.console.create_rectangle(self.order[7][0],125,self.order[7][1],250,outline="Black",fill=self.order[7][2])

        self.console.pack(side=tk.LEFT)
        return
    def motion(self, event):
      print("Mouse position: (%s %s)" % (event.x, event.y))
      return

    def execute(self, commandList):
        for item in commandList:
            self.body = 6000
            self.headTurn = 6000
            self.headTilt = 6000
            self.motors = 6000
            self.turn = 6000
            
            if(item == 0):
                self.motors = 5000
                self.tango.setTarget(MOTORS, self.motors)
                print("stuff")
                time.sleep(1)
                self.motors = 6000
                self.tango.setTarget(MOTORS, self.motors)
            elif(item == 1):
                self.turn = 5000
                self.tango.setTarget(TURNING, self.turn)
                print("stuff")
                time.sleep(1)
                self.turn = 6000
                self.tango.setTarget(TURNING, self.turn)
            elif(item == 2):
                self.headTilt = 5000
                self.tango.setTarget(HEAD_TILT, self.headTilt)
                print("stuff")
                time.sleep(1)
                self.headTilt = 6000
                self.tango.setTarget(HEAD_TILT, self.headTilt)
            elif(item == 3):
                self.headTurn = 5000
                self.tango.setTarget(HEAD_TURN, self.headTurn)
                print("stuff")
                time.sleep(1)
                self.headTurn = 6000
                self.tango.setTarget(HEAD_TURN, self.headTurn)
            elif(item == 4):
                self.body = 5000
                self.tango.setTarget(BODY, self.body)
                print("stuff")
                time.sleep(1)
                self.body = 6000
                self.tango.setTarget(BODY, self.body)
            time.sleep(1)

##---------------END GUI CLASS--------------------------------------

#--------MAIN--------------
win = tk.Tk()

gui = myGUI(win)
gui.controls()
gui.controls.bind('<ButtonPress-1>',gui.action)
gui.console()
