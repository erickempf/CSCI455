

class dialog():
    def __init__(self,text):
        
        self.text = text
        self.level = 0
        self.run = True

        self.top = []
        self.definitionsList = []

    def getLevel(self):
        return self.level

    def setLevel(self, newLevel):
        self.level = newLevel
        pass

    def definitions(self, name, choices):
        #DEFINE system here
        print("Definitions" + name)
        pass

    def proposition(self, command, robot):
        #Proposition work here
        print("Proposition")
        pass

    def options(self, command, human, robot):
        #Data structure here
        print(human)
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
        if line[0] == "#": # Comment
            print("Comment ignored")
            
        elif line[0] == "~": #Definition
            (name, choices) = line.split(":")
            self.definitions(name, choices)
            
        elif line[0] == "&": #Proposition
            (command, robot) = line.split(":")
            self.proposition(command.strip(), robot.strip())
            
        else:
            (command,human,robot) = line.split(":")
            self.options(command.strip(), human.strip(" ("), robot.strip())
            
        pass



##-------MAIN------

dialogEng = dialog("dialog.txt")

dialogEng.textIn()
##run = True
##while(run):
##    human = input()
##    human = human.lower()
##    if human == "exit":
##        run = False
##    print(human)
    



