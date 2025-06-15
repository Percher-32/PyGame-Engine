import json

class sm:
    def __init__(self,state):
        self.state = state
        self.states = []
        self.speed = 0
        self.leveledit = False
        self.work = True
        self.showui = False
        self.load = "plach"

    def update(self):
        if self.state == "game":
            self.states = ["test"]
            self.leveledit = False
            self.speed = 1
            self.showui = False
            self.showall = False
        if self.state == "editgame":
            self.states = ["test"]
            self.leveledit = True
            self.work = True
            self.speed = 1
            self.showui = True
            self.showall = True
        if self.state == "edit":
            self.states = ["Editor"]
            self.leveledit = True
            self.work = True
            self.speed = 0
            self.showui = True
            self.showall = True


