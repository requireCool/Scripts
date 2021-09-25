### Dianshijia - 电视家
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

**QuanX本地任务配置**
```
[task_local]
1 7,12,20 * * * https://gitee.com/requireCool/Scripts/raw/master/QuantumultX/Dianshijia/dianshijia.js
```

**QL环境变量**
| BoxJs             | QL          |
|-------------------|-------------|
| sy_signheader_dsj | DSJ_HEADERS |
| drawal_dsj        | DSJ_DRAWAL  |
>QL下好像有个任务不能完成，但总体上没有啥问题，建议还是在QuanX下跑
