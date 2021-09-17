# FGO_Bluetooth_Assistant
# 项目来源
https://github.com/McLaren12345/FGO_Bluetooth_Assistant
## 修改原因
2021.9月份更新了全屏功能模块,导致脚本定位有问题

## 使用方法
下载[虫洞](https://er.run/)

### 如何联系到我：
建议[B站私信联系](https://space.bilibili.com/6096019)。同时本人不会对诸如Python编程、代码修改等个人问题进行解答，仅接受bug反馈以及优化建议等内容的讨论。

## 具体修改说明
调整窗口,兼容Iphone12
完成部分
1. 战斗
2. 换人服
未修改
1. 友情池之类的功能 如 无限池 友情池 
2. 搓丸子
3. 战斗结束后的吃苹果 **(3天内完善代码)**
4. 其他衣服 **(极地,新年)**  注意
5. 角色,衣服的对象为敌方,此功能未实现

## 二.使用方法
1. 安装Python3.7  
2. 电脑可以操作后,鼠标放到任务栏 查看虫洞名称 修改配置文件 
```
目录调整
default_dir = r"G:\Documents\github\FGO_Bluetooth_Assistant"
template_path_str = "G:/Documents/github/FGO_Bluetooth_Assistant/Template/"
手机调整 暂且仅测试iphone12
const_phone = "iPhone12" 
修改虫洞程序名称 跟实际匹配
config = {"iPhone12":{"name":"Wormhole(iPhone)","length":1357,"bias":117}}
``` 
3. 调整技能,宝具  
```
character_skill(3,3,1) 3号使用3技能,目标1号位
character_skill(3,1) 3号使用1技能
Master_skill(Mystic_Codes.Chaldea_Combat_Uniform, 3,1,1)    换人1号和候补1号换
Master_skill(Mystic_Codes.Chaldea_Combat_Uniform, 1)    换人服1号技能
FGO_process(1,"Caster_Altria") 循环1次, 助战为C呆 Caster_Altria=>请查看template文件夹下的技能
```
4. python安装库
```
pip install opencv-python numpy twilio pywin32 pyserial
```
5. 运行`FGO_func`

