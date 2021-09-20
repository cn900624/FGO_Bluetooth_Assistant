import FGO_func as fc
import time
import sys
import Mystic_Codes
import Base_func_wormhole as Base_func
from Notice import sent_message
def FirstLevel():
    # 无限池1 阴间 仇凛+迦摩+2c呆
    # c呆
    fc.character_skill(3,3,1)
    fc.character_skill(3,2,1)
    fc.character_skill(3,1)
    # 换C呆
    fc.Master_skill(Mystic_Codes.Chaldea_Combat_Uniform,3,3,1)
    # 2号C呆
    fc.character_skill(3,3,1)
    fc.character_skill(3,2,1)
    fc.character_skill(3,1)
    # 仇凛
    fc.character_skill(1,1)
    fc.card()
    time.sleep(10)
    fc.WaitForBattleStart()
    # 第二T
    # 迦摩
    fc.character_skill(2,2)
    fc.character_skill(2,3)
    fc.card(2)
    time.sleep(10)
    fc.WaitForBattleStart()
    # 第三T
    fc.character_skill(1,2,2)
    fc.character_skill(1,3)
    fc.character_skill(2,1,1)
    fc.Master_skill(Mystic_Codes.Chaldea_Combat_Uniform,1)
    fc.card()

def wuzang():
     # 武藏
    fc.character_skill(1,2)
    # 无限池2 阳间 水武藏+2c呆 通杀所有阳间本
    # c呆
    fc.character_skill(3,3,1)
    fc.character_skill(3,2,1)
    fc.character_skill(3,1)
    # 2号C呆
    fc.character_skill(2,3,1)
    fc.character_skill(2,2,1)
    fc.character_skill(2,1)
    wuzangStatus,pos=Base_func.match_template("wuzangerror",False,0.75)
    if not wuzangStatus:
        print("skill error")
        sent_message("技能有问题")
        sys.exit()
    fc.card()
    time.sleep(10)
    fc.WaitForBattleStart()
    # 第二T
    fc.card()
    time.sleep(10)
    fc.WaitForBattleStart()
    # 第三T
    fc.character_skill(1,3)
    fc.card()

def ThirdLevel():
    # 无限池2 阳间 仇凛+2c呆+第五元素
    # c呆
    fc.character_skill(3,2,1)
    fc.character_skill(3,1)
    # 2号C呆
    fc.character_skill(2,2,1)
    fc.character_skill(2,1)
    fc.character_skill(1,3)
    # 仇凛
    fc.character_skill(1,1)
    fc.character_skill(1,3)
    # 第五元素
    fc.Master_skill(Mystic_Codes.The_Fifth_Element,3,1)
    fc.card()
    time.sleep(10)
    fc.WaitForBattleStart()
    # 第二T
    fc.character_skill(3,3,1)
    fc.card()
    time.sleep(10)
    fc.WaitForBattleStart()
    # 第三T
    fc.character_skill(2,3,1)
    fc.card()

def QigeSkills():
    # 无限池2 阴间 齐格3t 技能需求10-随意-6
    # 齐格
    fc.character_skill(1,1)
    # c呆
    fc.character_skill(3,3,1)
    fc.character_skill(3,2,1)
    fc.character_skill(3,1)
    fc.character_skill(2,3,1)
    fc.character_skill(2,2,1)
    fc.character_skill(2,1)
    # 怕释放失败导致np不足
    qigeskills,pos=Base_func.match_template("qigefail",False,0.75)
    if not qigeskills:
        print("skill error")
        sent_message("技能有问题")
        sys.exit()
    fc.card("qigeMain")
    time.sleep(10)
    fc.WaitForBattleStart()
    # 第二T
    # 换Cba
    fc.Master_skill(Mystic_Codes.Chaldea_Combat_Uniform,3,3,1)
    # cba
    fc.character_skill(3,3,1)
    fc.character_skill(1,3)
    fc.card("qigeMain")
    time.sleep(10)
    fc.WaitForBattleStart()
    # 第三T
    fc.character_skill(1,2)
    fc.character_skill(3,2)
    fc.Master_skill(Mystic_Codes.Chaldea_Combat_Uniform,1)
    fc.card("qigeMain")