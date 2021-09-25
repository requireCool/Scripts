### Youth - 中青阅读

| 名称             | 描述            | 状态 |
|----------------|---------------|----|
| youth.js       | 中青看点          | √  |
| youth_gain.js  | 中青看点(浏览赚+看看赚) | ×  |
| Youth_Read.js  | 中青自动阅读        | ×  |
| qx_rewrite.txt | 中青看点(获取CK、浏览赚、看看赚)-QX重写   | √  |
|qx_youthread.txt|中青自动阅读(获取浏览的文章body)-QX重写| √  |

**中青看点极速版的新版本抓不到ck，所以需要下载2.02版本的中青抓取ck**

**使用方法**
1. 重写-引用-资源路径 https://gitee.com/requireCool/Scripts/raw/master/QuantumultX/Youth/qx_rewrite.txt
2. 打开中青看点极速版2.02版本，点击我的-任务中心，圈x就会弹出获取ck成功
3. 到此就可以正常执行youth.js脚本了，但其中的阅读时长等内容经测试已经失效了，所以没写获取方法

**QuanX本地任务配置**
```
[task_local]
1 */5 * * * https://gitee.com/requireCool/Scripts/raw/master/QuantumultX/Youth/youth.js, enabled=true, tag=中青看点
30 6 * * * https://gitee.com/requireCool/Scripts/raw/master/QuantumultX/Youth/youth_gain.js, enabled=false, tag=中青看点浏览赚+看看赚
10 1-23 * * * https://gitee.com/requireCool/Scripts/raw/master/QuantumultX/Youth/Youth_Read.js, enabled=false, tag=中青阅读
```

**QL环境变量**

| BoxJs          | QL           |
|----------------|--------------|
| youthheader_zq | YOUTH_HEADER |

>教程参考自[Blu843](https://note.youdao.com/ynoteshare1/index.html?id=3a17dce54e83fd25a7a3de757b9b70cc&amp;type=note#/)，邀请码46700767