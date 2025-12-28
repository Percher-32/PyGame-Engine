import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import random
import pygame
import os





em = Gamemananager.em
tm = Gamemananager.tm
fm = Gamemananager.fm
om = Gamemananager.om
Tiled = Gamemananager.Tiled
cam =Gamemananager.cam
cm = Gamemananager.cm
sd = Gamemananager.sd
sm = Gamemananager.sm
um = Gamemananager.um
bg = Gamemananager.bg
pm = Gamemananager.pm






#SPAWNING
def spawnlaser(pos,speed,dir,enid,time,self,extraspeed=[0,0]):
    id = om.add(self,pos,"laser",dir,"HURT_laser",[1,1],univars.grandim,keepprev=1)
    om.objects[id]["type"] = "HURT_laser"
    movec = pygame.Vector2()
    movec.from_polar((speed,dir))
    movec +=  pygame.Vector2(extraspeed[0],extraspeed[1])
    om.set_value(id,"movec",movec)
    om.set_value(id,"speed",speed)
    om.set_value(id,"damage",5)
    om.set_value(id,"enid",enid)
    om.set_value(id,"extraspeed",extraspeed)
    om.set_value(id,"time",time)
    om.lighttoenemy(id,"l1",color=(255,0,20),colorinc=(0,0,0),nits=10,sizeinc=3,size=6,alphadec=6,alpha=60)


def spawnbiglaser(pos,time,speed,topspeed,self):
    id = om.add(self,pos,"rocket",0,"HURT_biglaser",[1.2,1.2],univars.grandim,keepprev=1)
    om.objects[id]["type"] = "HURT_biglaser"
    om.set_value(id,"tr",random.randint(30,60)/10)

    om.set_value(id,"maxtimer",time)
    om.set_value(id,"time",time)
    om.set_value(id,"canhome",1)
    om.set_value(id,"speed",speed + random.randint(-20,20))
    om.set_value(id,"topspeed",topspeed + random.randint(-20,0))
    om.set_value(id,"rot",0)
    om.lighttoenemy(id,"l1",color=(255,0,20),colorinc=(0,0,0),nits=10,sizeinc=3,size=6,alphadec=6,alpha=20)


def createhpbar(id,size,offset,self):
    """
        offset has y up = +\n
        Y axis FIXED
    """
    hpid = om.add(self,(0,0),"laser",0,"HPBAR",[size,size],univars.grandim,keepprev=1,layer=5)
    om.objects[hpid]["type"] = "HPBAR"
    om.objects[hpid]["rendercond"] = 0

    om.set_value(hpid,"obj-id",id)
    om.set_value(hpid,"size",size)
    om.set_value(hpid,"offset",offset)






#LOGIC FOR ENTITY
def damageable(id,dm,self,range = 200,functhrow = None,func = None):
    """
    Controls logic for making an object damagable by the player:
    
        NEEDED:
            Var : HP
    
    :param id: object-id
    :param dm: damage
    :param self: Game_manager
    :param range: IDK
    :param functhrow: functions to run when player throws object
    :param func: functions to run when player damages object
    """
    if self.flowstate:
        dm *= 2
    if len(self.attackerbox.keys()) > 0:
        if len(self.attackerbox["obj"]) > 0:
            if id in [i.name for i in self.attackerbox["obj"]]:
                if self.isthere("attack"):
                    if not self.isthere("damf" + id):
                        om.set_value(id,"HP",om.get_value(id,"HP") - dm)
                        self.wait("damf" + id,1)
                        om.set_value("player","dashmeter",om.get_value(id,"dashmeter") + 50)
                        om.set_value(id,"flashtimer",1)
                        if not func == None:
                            func()

    if self.isthere("skatego"):
        rad = 700
        if self.flowstate:
            rad *= 2
        if univars.func.dist(om.objects[id]["pos"],om.objects["skateboard"]["pos"]) < rad :

            if not self.isthere("damfthrow" + id):
                om.set_value(id,"flashtimer",1)
                self.wait("damfthrow" + id,1)
                om.set_value(id,"HP",om.get_value(id,"HP") - (dm*2))
                om.set_value("player","dashmeter",om.get_value(id,"dashmeter") + 100)

                if not functhrow == None:
                    functhrow()


                cm.setcond("playercam","shake",20)









#ENTITY FILE LOGIC
def entity_list_create(self):
    """
        Compiles all the enemy code and stres it in a dictionary
    """
    
    self.entity_type = os.listdir("Game_Code/Entities")
    self.entity_type = [entity for entity in self.entity_type if not ".py" in entity]


    self.entity_codes = {}
    for entity in self.entity_type:
        init_code = "NONE"
        main_code = "NONE"
        edit_code = "NONE"
        with open(f"Game_Code/Entities/{entity}/init.py","r") as init:
            init_code = init.read()
        with open(f"Game_Code/Entities/{entity}/main.py","r") as main:
            main_code = main.read()
            
            

        init_code = init_code.replace('self = "<REMOVE>"'," ")
        init_code = init_code.replace('id = "<REMOVE>"'," ")
        init_code = init_code.replace('info = "<REMOVE>"'," ")


        main_code = main_code.replace('self = "<REMOVE>"'," ")
        main_code = main_code.replace('id = "<REMOVE>"'," ")
        main_code = main_code.replace('info = "<REMOVE>"'," ")
        main_code = main_code.replace('st = "<REMOVE>"'," ")


        self.entity_codes[entity] = {"init":   compile(init_code,f"Game_Code/Entities/{entity}/init.py","exec"),"main":     compile(main_code,f"Game_Code/Entities/{entity}/main.py","exec")}
        
        
        
        
        if os.path.exists(f"Game_Code/Entities/{entity}/edit.py"):
            with open(f"Game_Code/Entities/{entity}/edit.py","r") as edit:
                edit_code = edit.read()
            
            edit_code = edit_code.replace('self = "<REMOVE>"'," ")
            edit_code = edit_code.replace('id = "<REMOVE>"'," ")
            edit_code = edit_code.replace('info = "<REMOVE>"'," ")
            

            self.entity_codes[entity]["edit"] = compile(edit_code,f"Game_Code/Entities/{entity}/edit.py","exec")


        if 'FLAG = "<PASS>"' in init_code.strip():
            self.entity_codes[entity]["init"] = "<PASS>"
        if 'FLAG = "<PASS>"' in main_code.strip():
            self.entity_codes[entity]["main"] = "<PASS>"
        if 'FLAG = "<PASS>"' in edit_code.strip():
            self.entity_codes[entity]["edit"] = "<PASS>"


def oncreate(id,info,self):
    """
        Runs compiled init.py file
    """

    if not hasattr(self,"entity_type"):
        self.entity_list_create()

    if info["type"] in self.entity_type:
        code = self.entity_codes[info["type"]]["init"]
        if not code == "<PASS>":
            exec(code,{"self":self,"id":id,"info":info})

def cond(id,info,st,self):
    """
        Runs compiled main.py file
    """
        
    if info["type"] in self.entity_type:
        code = self.entity_codes[info["type"]]["main"]
        if not code == "<PASS>":
            exec(code,{"self":self,"id":id,"info":info,"st":st})






def qrcond(id, info,self):
    """
        Runs compiled edit.py file
    """
    





        
    if info["type"] in self.entity_type:


        if "edit" in self.entity_codes[info["type"]].keys():
            code = self.entity_codes[info["type"]]["edit"]
            if not code == "<PASS>":
                exec(code,{"self":self,"id":id,"info":info})
                # self.print("WHY THE HELL AM I STILL HERE")






