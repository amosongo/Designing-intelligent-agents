#class person:
#    def __init__(self, name, number):
#        self.name = name
#        self.number = number
#class student (person):
#    def __init__(self, name, score, number):
#        person.__init__(self,name, number)
#        self.score = score
#    def display (self):
#        print("The student name is " + self.name)
#        print("The student score is ", self.score)
#        print("The student number is", self.number)

#s1 = student ("Arnold", 20, "JAD 34")
#s1.display ()
#s1 = student ("Kevin", 80, "JAD 35")
#s1.display ()

# Intelligent agents
########    simple reflex agent     ###############
#import random
#class environment(object):
#    def __init__(self):
#        self.location = ["A", "B"] # locations
#        self.locationcondition = {"A":"0", "B":"0"}
#        self.locationcondition["A"] = random.randint(0, 1)
#        self.locationcondition["B"] = random.randint(0, 1)
#        self.vacuumlocation = random.choice(self.location)
#class agent(environment):
#    def __init__(self, environment):
#        print("Environment condition", environment.locationcondition, "vacuum location",environment.vacuumlocation)
#        count = 0
#        while count < 2:
#            if environment.locationcondition [environment.vacuumlocation] == 1:
#                environment.locationcondition[environment.vacuumlocation] = 0
#                print(environment.vacuumlocation, "Has been cleaned")
#            else:
#                print(environment.vacuumlocation, "Is clean")
#            newindex = environment.location.index(environment.vacuumlocation) + 1
#            if newindex == 2:
#                newindex = 0
#            environment.vacuumlocation = environment.location[newindex]
#            count += 1
#        print(environment.locationcondition)
#e1 = environment()
#a1 = agent(e1)

###### Model Based Agent ######
#import random
#class environment(object):
#    def __init__(self):
#        self.location = ["A", "B"] # locations
#        self.locationcondition = {"A":"0", "B":"0"}
#        self.locationcondition["A"] = random.randint(0, 1)
#        self.locationcondition["B"] = random.randint(0, 1)
#        self.vacuumlocation = random.choice(self.location)
#        self.mode = ["T", "L"]
#        self.cleaningmethod = {"A":"T", "B":"T"}
#        self.cleaningmethod ["A"] = random.choice(self.mode)   #radnomizing the cleaningmethods
#        self.cleaningmethod ["B"] = random.choice(self.mode)
#class agent(environment):
#    def __init__(self, environment):
#        print("Environment condition", environment.locationcondition, "vacuum location",environment.vacuumlocation, "Cleaning method",environment.cleaningmethod)
#        count = 0
#        while count < 2:
#            if environment.locationcondition [environment.vacuumlocation] == 1:
#                if environment.cleaningmethod [environment.vacuumlocation] == "T":
#                   environment.cleaningmethod[environment.vacuumlocation] = "L"
#                else:
#                    environment.cleaningmethod[environment.vacuumlocation] = "T"
#                environment.locationcondition[environment.vacuumlocation] = 0
#                print(environment.vacuumlocation, "Has been cleaned")
#            else:
#                print(environment.vacuumlocation, "Is clean")
#            newindex = environment.location.index(environment.vacuumlocation) + 1
#            if newindex == 2:
#                newindex = 0
#            environment.vacuumlocation = environment.location[newindex]
#            count += 1
#        print("New conditions",environment.locationcondition)
#        print("updated history", environment.cleaningmethod)
#e1 = environment()
#a1 = agent(e1)

########## Goal Based Agents ############
#import random
#import time
#class environment(object):
#   def __init__(self):
#        self.location = ["A", "B"] # locations
#        self.locationcondition = {"A":"0", "B":"0"}
#        self.locationcondition["A"] = random.randint(0, 1)
#        self.locationcondition["B"] = random.randint(0, 1)
#        self.vacuumlocation = random.choice(self.location)
#        self.mode = ["T", "L"]
#        self.cleaningmethod = {"A":"T", "B":"T"}
#        self.cleaningmethod ["A"] = random.choice(self.mode)   #radnomizing the cleaningmethods
#        self.cleaningmethod ["B"] = random.choice(self.mode)
#class agent(environment):
#    def __init__(self, environment):
#        print("Environment condition", environment.locationcondition, "vacuum location",environment.vacuumlocation, "Cleaning method",environment.cleaningmethod)
#        count = 0
#        while count < 2:
#            if environment.locationcondition [environment.vacuumlocation] == 1:
#                if environment.cleaningmethod [environment.vacuumlocation] == "T":
#                   environment.cleaningmethod[environment.vacuumlocation] = "L"
#                else:
#                    environment.cleaningmethod[environment.vacuumlocation] = "T"
#                environment.locationcondition[environment.vacuumlocation] = 0
#                print(environment.vacuumlocation, "Has been cleaned")
#            else:
#                print(environment.vacuumlocation, "Is clean")
#            newindex = environment.location.index(environment.vacuumlocation) + 1
#            if newindex == 2:
#                newindex = 0
#            environment.vacuumlocation = environment.location[newindex]
#            count += 1
#        print("New conditions",environment.locationcondition)
#        print("updated history", environment.cleaningmethod)

#x = 0  # goal
#while x < 24:
#    e1 = environment()
#    a1 = agent(e1)
#    x += 1
#    time.sleep(1)

######### Utility based agents ###########
#import random
#import time
#class performance:
#    def __init__(self):
#        self.score = 0
#    def display(self):
#        print("Score: ", self.score)
#        print("Performance: ",(self.score/48)*100, "%")
#class environment(object):
#    def __init__(self):
#        self.location = ["A", "B"] # locations
#        self.locationcondition = {"A":"0", "B":"0"}
#        self.locationcondition["A"] = random.randint(0, 1)
#        self.locationcondition["B"] = random.randint(0, 1)
#        self.vacuumlocation = random.choice(self.location)
#        self.mode = ["T", "L"]
#        self.cleaningmethod = {"A":"T", "B":"T"}
#        self.cleaningmethod ["A"] = random.choice(self.mode)   #radnomizing the cleaningmethods
#        self.cleaningmethod ["B"] = random.choice(self.mode)
#class agent(environment, performance):
#    def __init__(self, environment, performance):
#        print("Environment condition", environment.locationcondition, "vacuum location",environment.vacuumlocation, "Cleaning method",environment.cleaningmethod)
#        count = 0
#        while count < 2:
#            if environment.locationcondition [environment.vacuumlocation] == 1:
#                if environment.cleaningmethod [environment.vacuumlocation] == "T":
#                   environment.cleaningmethod[environment.vacuumlocation] = "L"
#                else:
#                    environment.cleaningmethod[environment.vacuumlocation] = "T"
#                environment.locationcondition[environment.vacuumlocation] = 0
#                print(environment.vacuumlocation, "Has been cleaned")
#                performance.score += 1
#            else:
#                print(environment.vacuumlocation, "Is clean")
#            newindex = environment.location.index(environment.vacuumlocation) + 1
#            if newindex == 2:
#                newindex = 0
#            environment.vacuumlocation = environment.location[newindex]
#            count += 1
#        print("New conditions",environment.locationcondition)
#        print("updated history", environment.cleaningmethod)
#Thescore = performance()
#x = 0  # goal
#while x < 24:
#    e1 = environment()
#    a1 = agent(e1, Thescore)
#    x += 1
#    time.sleep(1)
#Thescore.display() # utility


########  Learning Agent  #########
#import random
#import time
#class performance:
#    def __init__(self):
#        self.score = 0
#    def display(self):
#        print("Score: ", self.score)
#        print("Performance: ",(self.score/48)*100, "%")
#        return (self.score/48)*100
#class environment(object):
#    def __init__(self):
#        self.location = ["A", "B"] # locations
#        self.locationcondition = {"A":"0", "B":"0"}
#        self.locationcondition["A"] = random.randint(0, 1)
#        self.locationcondition["B"] = random.randint(0, 1)
#        self.vacuumlocation = random.choice(self.location)
#        self.mode = ["T", "L"]
#        self.cleaningmethod = {"A":"T", "B":"T"}
#        self.cleaningmethod ["A"] = random.choice(self.mode)   #randomizing the cleaningmethods
#        self.cleaningmethod ["B"] = random.choice(self.mode)
#class agent(environment, performance):
#    def __init__(self, environment, performance):
#        print("Environment condition", environment.locationcondition, "vacuum location",environment.vacuumlocation, "Cleaning method",environment.cleaningmethod)
#        count = 0
#        while count < 2:
#            if environment.locationcondition [environment.vacuumlocation] == 1:
#                if environment.cleaningmethod [environment.vacuumlocation] == "T":
#                   environment.cleaningmethod[environment.vacuumlocation] = "L"
#                else:
#                    environment.cleaningmethod[environment.vacuumlocation] = "T"
#                environment.locationcondition[environment.vacuumlocation] = 0
#                print(environment.vacuumlocation, "Has been cleaned")
#                performance.score += 1
#            else:
#                print(environment.vacuumlocation, "Is clean")
#            newindex = environment.location.index(environment.vacuumlocation) + 1
#            if newindex == 2:
#                newindex = 0
#            environment.vacuumlocation = environment.location[newindex]
#            count += 1
#        print("New conditions",environment.locationcondition)
#        print("updated history", environment.cleaningmethod)
#Thescore = performance() # monitoring starts here
#x = 0  # goal
#t = 1
#while x < 24:
#    e1 = environment()
#    a1 = agent(e1, Thescore)
#    if x == 12:
#        p = Thescore.display()
#        if p > 50:
#            x = 0
#            t = 0.5
#            print("Increase visits, x and intervals, t")
#        else:
#            t = 2
#            x = 18 # we push x forward to 18 thus only 6 visits can be made
#            print("Reduce visits, x and intervals, t")
#    x += 1
#    time.sleep(1)
#Thescore.display() # utility


############ Problem Solving by Searching ########
# Town 1 - Town 2
#   |    -   |
# Town 3 - Town 4
import random
class environment(object):
    def __init__(self):
       self.location = ["1", "2", "3", "4"] # defining object
       self.move = ["U","D","L","R"] #different movement the agent can take
       self.path = {"1R": "2","1L": "W", "1U": "W", "1D": "3",
                    "2R": "W","2L": "1", "2U": "W", "2D": "4",
                    "3R": "4","3L": "W", "3U": "1", "3D": "W",
                    "4R": "W","4L": "3", "4U": "2", "4D": "W",}# allowed paths
       self.journey=[]
class agent(environment):
    def choosepath (self, agentlocation, environment): #methods belonging to this class
        i = random.choice(self.move)  # simulating the path
        j = str(agentlocation[0] + i)  # key used to detremine destination
        print("Suggested path: ", j)
        while environment.path[j] == "W":  # reject destination if its a Wall, W
            i = random.choice(self.move)  # simulating the path
            j = str(agentlocation[0] + i)  # key used to detremine destination
            print("Suggested path: ", j)
        print("Selected path: ", j)
        return j
    def take_journey (self, environment): # #design agent #inheriting attributes of environment
        agentlocation = random.choice(environment.location) #location
        print("Agent location: ", agentlocation)
        self.journey.append(agentlocation[0]) # starting point
        while agentlocation[0] != "4": # destination
            tomove = self.choosepath(agentlocation, environment) # keep moving code
            agentlocation[0]= self.choosepath(agentlocation, environment)
            agentlocation[0] = environment.path[tomove]
            self.journey.append(agentlocation[0])
        self.journey(4)
        print("journey", self.journey)
        return (self.journey)
e1 = environment()
a1 = agent()
a1.take_journey(e1)