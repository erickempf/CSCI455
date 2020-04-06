

class dialog():
    def __init__(self,text):
        
        self.text = text   # File name
        self.level = 0

        self.top = []
        self.definitionsList = [] #Definitions header location
        self.dialogList = [] #Saves all possible diaglog options

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
        entry = [command, human, robot]
        self.dialogList.append(entry)

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
            self.options(command.strip(), human.strip("( )"), robot.strip())
            
        else:
            print("Error")
            
        pass



##-------MAIN------

dialogEng = dialog("dialog.txt")

dialogEng.textIn()
for item in dialogEng.dialogList:
    for small in item:
        print(small)
    print("-----")
run = True
while(run):
    human = input()
    human = human.lower()
    if human == "exit":
        run = False
    for entry in dialogEng.dialogList:
        for item in entry:
            if human == item:
                print(entry[2])
                break
print("program finished")
    



