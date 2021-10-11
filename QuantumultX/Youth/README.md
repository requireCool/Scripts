### Youth - 中青阅读

| 名称             | 描述            | 状态 |
|----------------|---------------|----|
| youth.js       | 中青看点          | √  |
| youth_gain.js  | 中青看点(浏览赚+看看赚) | √  |
| youth_read.js  | 中青自动阅读        | √  |
| qx_rewrite.txt | 获取中青变量-QuantumultX重写   | √  |

**中青看点极速版的新版本抓不到ck，所以需要下载2.02版本的中青抓取ck**

**使用方法**
1. 重写-引用-资源路径 https://gitee.com/requireCool/Scripts/raw/master/QuantumultX/Youth/qx_rewrite.txt
2. 打开中青看点极速版2.02版本，点击我的-任务中心，QX就会弹出获取ck成功
3. 点开看看赚/浏览赚中的每一项，QX都会提示获取成功
4. 在首页随便点击文章，会提示文章获取成功/获取时长成功
5. 至此就完成了全部变量的获取

**QuanX本地任务配置**
```
[task_local]
1 0-1,6-23 * * * https://gitee.com/requireCool/Scripts/raw/master/QuantumultX/Youth/youth.js, enabled=true, tag=中青看点
10 8,12,16 * * * https://gitee.com/requireCool/Scripts/raw/master/QuantumultX/Youth/youth_gain.js, enabled=true, tag=中青看点浏览赚+看看赚
20 10,14,18 * * * https://gitee.com/requireCool/Scripts/raw/master/QuantumultX/Youth/youth_read.js, enabled=true, tag=中青自动阅读
```

**QL环境变量**

| BoxJs          | QL           |
|----------------|--------------|
| youthheader_zq | YOUTH_HEADER |
| youth_start | YOUTH_START |
| youth_look | YOUTH_LOOK |
| youth_autoread| YOUTH_READ |
| autotime_zq | YOUTH_TIME |
| 看教程抓包 | YOUTH_ARTBODY |

如果环境变量不对，就自己看教程吧

>教程参考自[Blu843](https://note.youdao.com/ynoteshare1/index.html?id=3a17dce54e83fd25a7a3de757b9b70cc&amp;type=note#/)，邀请码46700767