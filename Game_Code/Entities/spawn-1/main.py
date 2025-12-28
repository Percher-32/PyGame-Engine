import Managers.Gamemanager as Gamemananager
import Managers.univars as univars





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

def main(self,id,info,st):
    if om.get_value(id,"spawned") < om.get_value(id,"mp"):
        if univars.func.dist(om.objects[id]["pos"],om.objects["player"]["pos"]) < om.get_value(id,"ir"):
            om.set_value(id,"spawned",om.get_value(id,"spawned") + 1)

            nid = om.add(self,info["pos"],"enemy",0,"enemy-L",[1,1],univars.grandim,keepprev=1,info={"masterange":om.get_value(id,"or")})

            om.set_value(id,"sid",om.get_value(id,"sid") + [nid] )

            om.set_value(nid,"masterange",om.get_value(id,"or"))
					# print("nid",nid)

					# print("nid",nid,om.get_value(nid,"master_pos"))
				# om.objects[id]["type"] = "HURT:laser"




self = "<REMOVE>"
id = "<REMOVE>"
info = "<REMOVE>"
st = "<REMOVE>"



main(self,id,info,st)