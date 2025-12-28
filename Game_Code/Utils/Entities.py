import Managers.Gamemanager as Gamemananager
import Managers.univars as univars
import random
import pygame





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

def spawnlaser(self,pos,speed,dir,enid,time,extraspeed=[0,0]):
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


def spawnbiglaser(self,pos,time,speed,topspeed):
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


def createhpbar(self,id,size,offset):
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


def damageable(self,id,dm,range = 200,functhrow = None,func = None):
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

