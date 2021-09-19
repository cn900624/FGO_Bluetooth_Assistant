# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 22:50:06 2021

@author: Paul

This program is used for testing only
"""


# 测试代码

import Base_func_wormhole as Base_func
#import FGO_optional_func as op
import Serial_wormhole as Serial
import FGO_func as fc
import time
import Mystic_Codes
import selfSkill
import sys
Base_func.init_wormhole()
times=1
#确保没有非C呆的好友 按照HP/ATK排序进一步确保
#助战
#无限池抽取函数
for s in range(8):
    Serial.mouse_set_zero()
    Serial.mouse_move((316,250))
    for i in range(46):
        Serial.mouse_click()
        time.sleep(0.5)
        Serial.mouse_click()
        time.sleep(0.5)
    print("当次结束"+str(s))
    resetUnLimit,Position = Base_func.match_template("resetUnLimit")
    if resetUnLimit:
        Serial.touch(728, 128) #重置
        time.sleep(1)
        Serial.touch(532, 312) #重置确认
        time.sleep(3)
        Serial.touch(425, 309) #重置成功
        time.sleep(1)
ent_message("无限池抽完了")
sys.exit(0)

for i in range(times):
   # selfSkill.FirstLevel()
    # fc.character_skill(3,3,1)
    #fc.character_skill(3,2,1)
    #fc.character_skill(3,1)
    #换C呆c
    fc.Master_skill(Mystic_Codes.Chaldea_Combat_Uniform,3,3,1)
    #2号C呆
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

    print(1)
    # skill,poisitionSkill=Base_func.match_template(casterSkillImg)
    # #技能不满足时候
    # while not(skill):
    #     print("找不到C呆")
    #     Serial.mouse_move((514,74))   #refresh     
    #     time.sleep(0.5)
    #         #Flag,Position = Base_func.match_template('Refresh_decide')
    #     Serial.mouse_move((541,310))   #decide
    #     time.sleep(0.5)
    #     #Flag,Position = Base_func.match_template('Refresh_decide')

    #     skill,poisitionSkill=Base_func.match_template(casterSkillImg)
    #     time.sleep(3)
    # #找到了
    
    # print("fount c")
    # Serial.mouse_move((poisitionSkill[0],poisitionSkill[1]))
    # #开打
    # time.sleep(1.5) 
    # Serial.mouse_move((773,371))
    # print("game begin")
    # time.sleep(8)                          #等待战斗开始
    # fc.WaitForBattleStart()
    # print("skill begin")
# #测试技能距离
#     character_nos=[1,2,3]
#     skill_nos=[1,2,3]
#     for character_no in character_nos:
#         for skill_no in skill_nos:
#             Serial.mouse_move((66+(character_no-1)*175+(skill_no-1)*50,306))

# #end
# #测试技能目标
#     character_nos=[1,2,3]
#     for character_no in character_nos:
#         Serial.mouse_move((246+(character_no-1)*175,245))

# #end


print("all end")
#Serial.mouse_move(1,2)
# 若无好友 则GG
#time.sleep(2)
#Base_func.match_template("Caster_Altria_skill_level")
#op.match_template("Caster_Altria_skill_level")
# op.FriendPointSummon(2.5)
# for i in range(10):
#     op.Upgrade()
#     op.FriendPointSummon()



# fusea = Base_func.Fuse()
# fusea.increase()


#Base_func.match_template('Maxlvl')

#(790,215) (125,330) (125,450)

#Serial.mouse_swipe((125,210),(125,580),0.5)


# def material_select():
#     Serial.mouse_move((125,210))
#     Serial.mouse_hold()
#     time.sleep(1)       #1.5 originally
#     Serial.mouse_move((790,215))
#     Serial.mouse_move((125,330))
#     Serial.mouse_move((125,450))
#     Serial.mouse_move((125,580))
#     time.sleep(0.5)
#     Serial.mouse_release()


