## Anti Forward Bot
本Bot用于让你眼不见心不烦群内某些转发来源为某些频道的内容。

### 部署环境
Python 3.6+  
pyrogram 0.16.0  
1. 在 Linux 下执行此指令安装 pyrogram:  
```
pip3 install -U pyrogram tgcrypto
```  
2. 从 [BotFather](https://t.me/BotFather) 申请得到您的 API Token ，从 [API Settings](https://my.telegram.org/apps) 申请得到您的 API Hash 和 API ID，并将它们填入 `config.json` 里。  
3. 对于你不想在群内看到的频道，请按照`-100114514191`的格式填入`channels.json`的方括号内，每个频道用逗号隔开。  
4. 要在群组内启用删除功能，请先在 [BotFather](https://t.me/BotFather) 处关闭隐私模式  
（步骤为:/mybots -> Bot Settings -> Group Privacy -> Turn off)

### 开源协议
本程序使用MIT协议开源