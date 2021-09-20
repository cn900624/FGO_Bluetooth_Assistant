# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:51:36 2019

@author: McLaren
"""
import time
import sys
import random
import Serial_wormhole as Serial 
import Base_func_wormhole as Base_func
import Mystic_Codes
import Global_Config as gc
import selfSkill
import datetime
from Notice import sent_message



sys.path.append(gc.default_dir) 
fuse = Base_func.Fuse()

# 异常时候的处理
# 空白区域点击指定次数
def errorAction():
    # 随意点击几次
    Serial.touch(72,70,gc.clickRestCount) 
    #角色详情页面关闭按钮
    #Serial.touch(677,32) 
    #换人礼装技能关闭按钮
    #Serial.touch(677,32) 
    time.sleep(0.4)   

def enter_battle():
    # menuFlag,Position1 = Base_func.match_template("Menu_button")
    reenterFlag,Position2 = Base_func.match_template("reenter_battle")
    #print('Flag now: ', menu, "Position now: ", Position )   
    
    while not(reenterFlag):
        time.sleep(1)       #Original value is 1
        #menuFlag,Position1 = Base_func.match_template("Menu_button")
        reenterFlag,Position2 = Base_func.match_template("reenter_battle")
        fuse.increase()
        fuse.alarm()        
    fuse.reset()
    
    # if menuFlag:
    #     LastOrderFlag,Position3 = Base_func.match_template("LastOrder_sign")
    #     if LastOrderFlag:
    #         Serial.touch(Position3[0],Position3[1])
    #         print("Entered last order success")
    #         return "LastOrder"
    #     else:
    #         Serial.touch(791,155)
    #         print("Entered default success")
    #         return "Default"
    if reenterFlag:
        Serial.touch(Position2[0],Position2[1]) 
        return "Reenter"
    else:
        print("ReadyToBattle Error")
        sent_message()
        sys.exit(0)
        
        
def WaitForBattleStart():
    Flag,Position = Base_func.match_template("Attack_button")
    while not(Flag):
        time.sleep(1)        
        Flag,Position = Base_func.match_template("Attack_button")  
        fuse.increase()
        fuse.alarm()
    fuse.reset()
    time.sleep(0.2) 

        
def WaitForFriendShowReady():
    friendFlag,Position = Base_func.match_template("friend_sign")
    noneFlag,Position2 = Base_func.match_template("no_friend")    
    while not(friendFlag or noneFlag):
        time.sleep(1)       
        friendFlag,Position = Base_func.match_template("friend_sign")
        noneFlag,Position2 = Base_func.match_template("no_friend")
        fuse.increase()
        fuse.alarm()
    fuse.reset()

    
def apple_feed(): 
    
    time.sleep(1.5)
    recoverFlag,Position = Base_func.match_template("Gold_apple")
    if not(recoverFlag):
        return
    
    goldFlag,goldPosition = Base_func.match_template("Gold_apple")
    if goldFlag:
        Serial.touch(goldPosition[0]+80,goldPosition[1])
        time.sleep(1.5)                
        Serial.touch(550,313) #决定
        gc.num_GoldApple_used += 1
        print(" Feed gold apple success")
        return

    silverFlag,silverPosition = Base_func.match_template("Silver_apple")          #check similarity between highlight and normal icon   
    if silverFlag:
        Serial.touch(silverPosition[0]+80,silverPosition[1])
        time.sleep(1.5)            
        Serial.touch(550,313)   #决定
        gc.num_SilverApple_used += 1
        print(" Feed silver apple success")
        return
    
    Serial.touch(0,0)     
    sent_message()           
    sys.exit(0)
        
        
def find_friend(servant):
    WaitForFriendShowReady()    
    foundFlag,Position = Base_func.match_template(servant+"_skill_level")
    attemptnum = 1
    #找310CBA直到找到为止
    while not(foundFlag):
        #Flag,Position = Base_func.match_template('Refresh_friend')
        Serial.touch(514,74)   #refresh     
        time.sleep(0.5)
        #Flag,Position = Base_func.match_template('Refresh_decide')
        Serial.touch(541,310)   #decide
        WaitForFriendShowReady()   
        foundFlag,Position = Base_func.match_template(servant+"_skill_level")
        attemptnum += 1
        time.sleep(3) 
        
    Serial.touch(Position[0],Position[1]-60)
    time.sleep(1.5)               

     
def budao():   
    finFlag = False
    attackFlag = False
    while not(finFlag):
        Serial.touch(730,335)   #点击attack按钮 
        time.sleep(1)       
        Card_index = random.sample(range(0,4),3) #随机三张牌   
        Serial.touch(141+(Card_index[0])*152,285)          
        Serial.touch(141+(Card_index[1])*152,285)  
        Serial.touch(141+(Card_index[2])*152,285)
        while not(finFlag or attackFlag):
            finFlag,Position = Base_func.match_template("Battlefinish_sign")
            attackFlag,Position = Base_func.match_template("Attack_button")
 
        
def quit_battle():
    time.sleep(15)
    finFlag,Position = Base_func.match_template("Battlefinish_sign")
    attackFlag,Position = Base_func.match_template("Attack_button")
    while not(finFlag or attackFlag):
        finFlag,Position = Base_func.match_template("Battlefinish_sign")
        attackFlag,Position = Base_func.match_template("Attack_button")
    if finFlag:
        pass
    elif attackFlag:
        print(" 翻车，进入补刀程序")          #翻车检测
        budao()
    time.sleep(1)
    rainbowFlag,Position = Base_func.match_template("Rainbow_box")  #检测是否掉礼装，若掉落则短信提醒  
    if rainbowFlag:
        gc.num_Craft += 1
        sent_message("打到礼装了!")
    Serial.touch(725,350,6)    
    Serial.touch(266,343,2)                #拒绝好友申请
    Serial.mouse_set_zero()         #鼠标复位,防止误差累积
    time.sleep(1)


#improve        
def Master_skill(func = Mystic_Codes.Chaldea_Combat_Uniform, *args,isErrTry=False):
    time.sleep(0.2)  
    Serial.touch(780,180)               #御主技能按键
    func(*args)
    #若技能释放失败，则空白处多点几次看是否能把技能纠正回来
    attackFlag,Position = Base_func.match_template("Attack_button")
    errCheck,PositionErr= Base_func.match_template("error1")
    # 正常应该没有攻击按钮
    if attackFlag or errCheck:
        print("master释放失败")
        errorAction()
        # 关闭错误页
        if errCheck:
            Serial.touch(PositionErr[0],PositionErr[1]) 
            time.sleep(0.3)
        if not isErrTry:#防止无限重复
            Master_skill(func,*args,True)
        else:
            print("master再次释放失败")
            sys.exit()
    #仅成功要等待
    if not isErrTry:
        WaitForBattleStart()
        time.sleep(1)
    
def character_skill(character_no,skill_no,para=None,isErrTry=False):   #角色编号，技能编号，选人（可选）
    charPos = (66+(character_no-1)*175+(skill_no-1)*50,306)
    Serial.touch(charPos[0],charPos[1])    
    if para != None:
        targetPos = (246+(para-1)*175,245)  #技能选人
        Serial.touch(targetPos[0],targetPos[1])    
    time.sleep(0.2)   
    #若技能释放失败，则空白处多点几次看是否能把技能纠正回来
    attackFlag,Position = Base_func.match_template("Attack_button")
    errCheck,PositionErr= Base_func.match_template("error1")
    # 正常应该没有攻击按钮
    if attackFlag or errCheck:
        print("技能释放失败")
        errorAction()
        # 关闭错误页
        if errCheck:
            Serial.touch(PositionErr[0],PositionErr[1]) 
            time.sleep(0.3)
        if not isErrTry:#防止无限重复
            character_skill(character_no,skill_no,para,True)
        else:
            print("技能再次释放失败")
            sys.exit()
    #仅成功要等待
    if not isErrTry:
        time.sleep(2.5)         #等待技能动画时间
        WaitForBattleStart()


    

    
def card(successImg,NoblePhantasm_no=1,isErrTry=False):    
    # 769,369 宝具返回按钮位置
    Serial.touch(730,335)   #点击attack按钮 
    time.sleep(2)       
    Serial.touch(300+(NoblePhantasm_no-1)*140,63)   #打手宝具,参数可选1-3号宝具位
    Card_index = random.sample(range(0,4),2) #随机两张牌   
    Serial.touch(141+(Card_index[0])*152,285)          
    time.sleep(0.1) 
    successImgFlag,Position = Base_func.match_template(successImg)
    Serial.touch(141+(Card_index[1])*152,285)  
    attackFlag,Position = Base_func.match_template("Attack_button")
    # 宝具没被选中 
    if not successImgFlag:
        print("宝具释放失败")
        # 不在点击攻击页面 则额外按返回攻击页面
        if not attackFlag:
            #返回攻击页面
            Serial.touch(769,369)
            time.sleep(1)
        #重置点击
        errorAction()
        #重新选择宝具
        
        if not isErrTry:#防止无限重复
            card(successImg,NoblePhantasm_no,True)
        else:
            print("宝具再次释放失败")
            sys.exit()
    
def battle(): 
    #判断是否进入战斗界面
    
    Serial.touch(773,365)      
    time.sleep(6)                          #等待战斗开始
    WaitForBattleStart()  
    Serial.mouse_set_zero()         #鼠标复位,防止误差累积  
    time.sleep(0.5)   
    # time.sleep(6)                   #等待6秒，因为礼装效果掉落暴击星会耗时
    # selfSkill.SecondLevel() #设定好的技能模块
    selfSkill.QigeSkills()

def FGO_process(times=1,servant="CBA"):
    for i in range(times):
        start = time.time()
        times-=1
        
        find_friend(servant)
        battle()        
        quit_battle()                
        print(" {}times of battles remain.".format(times))
        print(" Currently {} Gold Apples, {} Silver Apples used, {} Crafts droped.".format(gc.num_GoldApple_used,gc.num_SilverApple_used,gc.num_Craft))
        enter_battle()
        if times>0:
            apple_feed()
        end = time.time()
        print("打一次本大概花了"+str(int(end-start))+"秒")

def main():
    #Serial.port_open(port_no)   #写入通讯的串口号
    #sent_message("begin play games")
    Base_func.init_wormhole()
    Serial.mouse_set_zero()
    FGO_process(10,"Caster_Altria")
    #Serial.port_close()
    print(" All done!") 
    sent_message("all done!")
        
if __name__=="__main__":
	main()


