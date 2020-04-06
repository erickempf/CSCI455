class entry():

    def __init__(self, command, human, robot):

        self.command = command
        self.human = human
        self.robot = robot
        self.children = []
        self.parent = None


class dialog():
    def __init__(self,text):
        
        self.text = text   # File name
        self.level = 0

        self.top = []
        self.definitionsList = [] #Definitions header location
        self.dialogList = [] #Saves all possible diaglog options
        self.recentEntry = entry(0,"error","error")
        self.validinput = []

    def getLevel(self):
        return self.level

    def setLevel(self, newLevel):
        self.level = newLevel
        pass

    def definitions(self, name, choices): # Handles DEfintions
        #DEFINE system here
        #print(name)
        pass

    def proposition(self, command, robot): # Handles Propositions
        #Proposition work here
        print("Proposition")
        pass

    def options(self, command, human, robot): # Handles all other dialog
        entry1 = entry(command, human, robot)
        if entry1.command == 0:
            self.dialogList.append(entry1)
            self.validinput.append(human)
            #print("if1")
        elif command == self.recentEntry.command+1:
            self.recentEntry.children.append(entry1)
            entry1.parent = self.recentEntry
            #print("if2")
        elif command == self.recentEntry.command:
            parent = self.recentEntry.parent
            parent.children.append(entry1)
            entry1.parent = parent
            #print("if3")
        else:
            while(self.recentEntry.command >= command):
                self.recentEntry = self.recentEntry.parent
            self.recentEntry.children.append(entry1)
            entry1.parent = self.recentEntry
            #print("if4")
        self.recentEntry = entry1
        #print(entry1.command)

    def textIn(self):           #Reads in the file text
        file = open(self.text,"r")
        for x in file:
            self.line = x
            self.dialog(self.line)
        file.close()        
        pass

    def dialog(self, line): #Splits into proper dialog parts
        line = line.strip() #Removes leading and trailing spaces
        line = line.lower() #takes it to all lowercase
        if line[0] == "#": # Comment
            print("Comment ignored")
            
        elif line[0] == "~": #Definition
            (name, choices) = line.split(":")
            self.definitions(name.lstrip("~"), choices)
            
        elif line[0] == "&": #Proposition
            (command, robot) = line.split(":")
            self.proposition(command.strip(), robot.strip())
            
        elif line[0].lower() == "u":
            (command,human,robot) = line.split(":")
            command = command.strip("u")
            if command == "":
                command = "0"
            command = int(command)
            self.options(command, human.strip("( )"), robot.strip())
            
        else:
            print("Error")
            
        pass



##-------MAIN------

dialogEng = dialog("dialog.txt")

dialogEng.textIn()
run = True
while(run):
    human = input()
    human = human.lower()
    if human == "exit":
        run = False
    elif human in dialogEng.validinput:
        for entry in dialogEng.dialogList:
            if entry.human == human:
                print(entry.robot)
                if entry.children != []:
                    currentEntry = entry
                    dialogEng.level += 1
                    while dialogEng.level != 0:
                        validinputs = []
                        for child in currentEntry.children:
                            validinputs.append(child.human)
                        human = input()
                        if human in validinputs:
                            for child in currentEntry.children:
                                if child.human == human:
                                    print(child.robot)
                                    currentEntry = child
                                    if currentEntry.children != []:
                                        dialogEng.level +=1
                                    else:
                                        dialogEng.level = 0
                        elif human == "exit":
                            dialogEng.level = 0
                            run = False
                        else:
                            print("Invalid input")                        
    else:
        print("Invalid input")
        
print("Goodbye. Program finished")
    



