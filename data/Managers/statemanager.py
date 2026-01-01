import json

class sm:
    def __init__(self,state):
        self.state = state
        self.states = []
        self.speed = 0
        self.leveledit = False
        self.work = True
        self.showui = False
        self.showall = False  
        self.cammove = False
        self.load = "plach"

    def update(self):
        if self.state == "debugame":
            self.states = "game"
            self.leveledit = False
            self.speed = 1
            self.showui = False
            self.work = True
            self.showall = False
            self.cammove = False
        if self.state == "game":
            self.states = "game"
            self.leveledit = False
            self.speed = 1
            self.showui = False
            self.work = False
            self.showall = False
            self.cammove = False
        if self.state == "editgame":
            self.states = "game"
            self.leveledit = True
            self.work = True
            self.speed = 1
            self.showui = True
            self.showall = False
            self.cammove = True
        if self.state == "edit":
            self.states = "Editor"
            self.leveledit = True
            self.work = True
            self.speed = 0
            self.showui = True
            self.showall = True
            self.cammove = True
        if self.state == "uitest":
            self.states = "veiw"
            self.leveledit = False
            self.speed = 1
            self.showui = False
            self.work = True
            self.showall = False
            self.cammove = True
        if self.state == "featest":
            self.states = "test"
            self.leveledit = True
            self.speed = 1
            self.showui = False
            self.work = True
            self.showall = False
            self.cammove = True
        if self.state == "test":
            self.states = "null"
            self.leveledit = False
            self.speed = 1
            self.showui = True
            self.work = True
            self.showall = False
            self.cammove = True
        
