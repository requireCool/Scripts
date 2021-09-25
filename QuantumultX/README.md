# Scripts for QuantumultX

### 首先要做的
```
BoxJs配置连接 https://chavyleung.gitbook.io/boxjs/

BoxJs订阅链接 https://gitee.com/requireCool/Scripts/raw/master/QuantumultX/sunert.boxjs.json
```
### 1. Youth - 中青阅读

| 名称             | 描述            | 状态 |
|----------------|---------------|----|
| youth.js       | 中青阅读          | √  |
| youth_gain.js  | 中青看点(浏览赚+看看赚) | ×  |
| Youth_Read.js  | 中青自动阅读        | ×  |
| qx_rewrite.txt | 中青阅读(获取CK、浏览赚、看看赚)-QX重写   | √  |
|qx_youthread.txt|中青自动阅读(获取浏览的文章body)-QX重写| √  |

**中青看点极速版的新版本抓不到ck，所以需要下载2.02版本的中青抓取ck**

**使用方法**
1. 重写-引用-资源路径 https://gitee.com/requireCool/Scripts/raw/master/QuantumultX/Youth/qx_rewrite.txt
2. 打开中青看点极速版2.02版本，点击我的-任务中心，圈x就会弹出获取ck成功
3. 到此就可以正常执行youth.js脚本了，但其中的阅读时长等内容经测试已经失效了，所以没写获取方法
>教程参考自[Blu843](https://note.youdao.com/ynoteshare1/index.html?id=3a17dce54e83fd25a7a3de757b9b70cc&amp;type=note#/)，邀请码46700767

### 2. Dianshijia - 电视家
| 名称            | 描述  | 状态 |
|---------------|-----|----|
| dianshijia.js | 电视家 | √  |
| qx_rewrite.txt | 电视家获取CK、提现地址 | √ |

**电视家的新版本抓不到信息，要用老版本的，经测试1.85可以使用**

**使用方法**
1. 重写-引用-资源路径 https://gitee.com/requireCool/Scripts/raw/master/QuantumultX/Dianshijia/qx_rewrite.txt
2. 打开电视家1.85版本，点击底部领现金，圈X会弹出获取CK成功
3. 点击'去提现'，然后点击任意提现金额-立即提现，圈X会提示获取提现地址成功
4. 在BoxJs中`应用-电视家`选择下次签到奖励，保存，回到圈X设置定时，OK
