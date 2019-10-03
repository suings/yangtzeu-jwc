# yangtzeu-jwc

长江大学教务处(jwc.yangtzeu.fun)移动端代码

# 使用引导
## 环境安装
需求环境: `python3`,`requests`,`flask`
```
pip install -r requirements.txt
```
## 启动
```
python app.py
```

## 单独获取课表
首先修改kb.py中的账号信息,然后执行`python kb.py`即可
```
user = ""
pwd  = ""
=>
user = "你的学号"
pwd  = "你的密码"
```

```
python kb.py
```
# 开放API(短期可用)
```
POST http://jwc.yangtzeu.fun/api
```
调用地址: http://jwc.yangtzeu.fun/api

请求方式: POST

返回类型: JSON

请求格式: 
formdata: 
{
        "username" : "学号",
        "password" : "密码"
}
## 正常返回示例
```
{
        "status": "正常",
        "info": "周是从第0周开始的",
        "data": [
                [
                        "东13-B-408c",
                        "离散数学",
                        4,
                        1,
                        "01111111111111111100000000000000000000000000000000000"
                ]
        ]
}
```
# 文件说明
```text
./
│  .gitignore
│  app.py # flask程序
│  kb.py # 课表爬取程序
│  LICENSE
│  README.md
│  requirements.txt # 第三方依赖
│
├─static
│      bg.jpg
│      public.js # 两个页面的公用js
│
└─templates
        index.html # 登录页面
        kb.html # 课表显示
```

# 注意
- index.html中默认会检测是否为移动端并跳转到相应页面,调试时可设置机型为mobile,或者去除相应代码
- 国庆期间发现官方教务处间断性不能访问,可能会导致kb.py中代码无效
- kb.py及kb.html中的参数只适用于2019年下半学期,若超出此学期,将产生预期之外的错误,本仓库未必会随时间更新
# QQ群
点击链接加入群聊<a href="https://jq.qq.com/?_wv=1027&k=5WRmsqn">【长江大学编程交流】</a> 

群号: 982198236
