# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 22:16:33 2021

@author: Paul
"""
import win32con, win32api


default_dir = r"E:\Documents\GitHub\FGO_Bluetooth_Assistant"
template_path_str = "E:\Documents\GitHub\FGO_Bluetooth_Assistant/Template/"
const_phone = "iPhone12"
isPushMsg = False

# bias:游戏蓝条宽度 9.3更新后为0 
# 21 虫洞宽 16高
# 1080*607    leng-2*bias-2*21=1080  649-16-26=607
# 864*400  宽 

config = {"iPhone12":{"name":"Wormhole(iPhone)","length":906,"bias":0}}
wormholeHeight=20
wormholeWeight=21
const_position = win32api.GetSystemMetrics(win32con.SM_CXSCREEN) - \
                    (config[const_phone]["length"]  - wormholeWeight)
const_interface_origin = (const_position+wormholeWeight, 0+wormholeHeight)


num_GoldApple_used = 0
num_SilverApple_used = 0
num_Craft = 0


enhancedFilterInit_bool = True
materialFilterInit_bool = True
servantFilterInit_bool = True



#请修改变量default_dir，template_path_str，const_phone
#default_dir为你的程序根目录
#template_path_str可通过下方函数得到，函数参数为修改后的default_dir，结果输出在终端
#const_phone为你的设备型号，config有待完善

'''
def path_str(root_dir):
    local_str = list(root_dir)
    for i in range(len(root_dir)):
        char = root_dir[i]
        if char == "\\":
            local_str[i] = "/"
    local_str = ''.join(local_str)
    local_str += "/Template/" 
    print(local_str)
    return local_str       
    


path_str(default_dir)
'''