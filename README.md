# FGO_Bluetooth_Assistant
# 项目来源
https://github.com/McLaren12345/FGO_Bluetooth_Assistant
## 修改原因
2021.9月份更新了全屏功能模块,导致脚本定位有问题
## 项目说明
仅支持IOS 其他手机等待原作者 可能适配除Iphone12以外手机,暂无测试条件  
FGO,自动打本,吃苹果,抽友情池,无限池  
注意 战斗只支持3T稳定 至多补刀4T  
不支持4T及以上打本  第4T只会随机砍3刀
- [x] 选助战,战斗,继续战斗,体力不足自动吃苹果
- [x] 换人服
- [x] 无限池抽取
- [ ] 第五元素(未测试)
- [ ] 友情池抽取(2021.9.30前完成)
- [ ] 搓丸子,其他功能(不准备适配,请等待原作者完善)
## 使用方法
下载[虫洞](https://er.run/)
## 建议环境
蓝牙和手机放的近点  
不要有其他蓝牙设备 防止干扰引起错位
手机可以连接2.4网络，应该不会和5g蓝牙冲突(未研究具体)
经测试 稳定运行10次+(当中有一次不知道为什么切回主界面了 手动切回后正常)
### 如何联系到我：
建议 邮件 <zhf883680@gmail.com> 。同时本人不会对诸如Python编程、代码修改等个人问题进行解答，仅接受bug反馈以及优化建议等内容的讨论。

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
config = {"iPhone12":{"name":"Wormhole(iPhone)","length":906,"bias":0}}
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
5. 在选择助战页面运行`FGO_func`

