# Archive

## List
|Name|Discription|Status|
|---|---|---|
|jd_bean_sign.js|lxk的京东多合一签到|可用|
|jd_blueCoin_new.py|python版的京东超市兑换|可用|
|long_half_redrain.js|longzhuzhu的半点红包雨|可用|
|long_super_redrain.js|longzhuzhu的整点红包雨|可用|
|jd_angryBean.js|cdle的抢京豆|可用|
|jd_goodMorning.js|cdle的早起福利|可用|
|jd_ckcheck.js|MoneyMr的ck到期时间检查工具，要配合面板用|可用|
|sendNotify.js|MoneyMr的推送脚本，可以实现黑名单活动不推送消息|可用|

## Use

* #### For sendNotify.js
  1. 通知黑名单 `export NOTIFY_SKIP_LIST="店铺签到&京东手机狂欢城"`
  2. 配合`account.json`（例如下），将原有的的`sendNotify.js`修改为`sendNotify2.js`可以实现一对一推送
```
[
    {
        "pt_pin": "xxxxxx",
        "remarks": "xxxx",
        "PUSH_PLUS_TOKEN": "xxxx",
        "go_cqhttp_qq": "",
        "go_cqhttp_method": "send_private_msg",
        "TG_USER_ID": ""
    },
    {
        "pt_pin": "xxxx",
        "remarks": "xxxx",
        "PUSH_PLUS_TOKEN": "xxxx",
        "go_cqhttp_qq": "",
        "go_cqhttp_method": "send_private_msg",
        "TG_USER_ID": ""
    }
]
```
