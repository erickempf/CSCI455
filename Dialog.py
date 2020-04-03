

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

    def textInt(self):
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
            command.strip()
            human.strip()
            robot.strip()
            
        
        pass



##-------MAIN------

dialogEng = dialog("dialog.txt")

dialogEng.textInt()



