

class dialog():
    def __init__(self,text):
        
        self.text = text
        self.level = 0

        self.top = []
        self.definitions = []

    def getLevel(self):
        return self.level

    def setLevel(self, newLevel):
        self.level = newLevel
        pass

    def definitions(self):
        #DEFINE system here
        
        pass

    def proposition(self, name, choices):
        pass

    def options(self, command, human, robot):
        pass

    def textIn(self):
        file = open(self.text,"r")
        for x in file:
            self.line = x
            self.dialog(self.line)
        file.close()        
        pass

    def dialog(self, line):
        line = line.strip() #Removes leading and trailing spaces
        line = line.lower() #takes it to all lowercase
        if line[0] == "#":
            print("Comment ignored")
        elif line[0] == "~":
            (name, choices) = line.split(":")
            self.defintions(name,choices)
        elif line[0] == "&":
            (command, robot) = line.split(":")
            self.proposition(robot)
        else:
            (command,human,robot) = line.split(":")
            command.strip()     #Rid of any spaces
            human.strip()   
            robot.strip()
            self.options(command, human, robot)
        pass



##-------MAIN------

dialogEng = dialog("dialog.txt")

dialogEng.textIn()



