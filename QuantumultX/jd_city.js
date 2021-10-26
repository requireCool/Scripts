let code = $.getdata('jd_city_withdraw_code')

if (isGetInfo = typeof $request !== 'undefined') {
    GetInfo();
    $.done()
}

function GetInfo() {
    if ($request && $request.method != 'OPTIONS' && $request.url.match(/\/client\.action/)) {
        const headerVal = JSON.stringify($request.headers);
        const cookie = headerVal['cookie']
        $.log(`headerVal:${headerVal}`);
        if (headerVal) $.setdata(cookie, 'jd_city_withdraw_cookie')
        $.msg($.name, `获取Cookie: 成功`, ``)
        
        const reqBody = $request.body;
        const codeVal = reqBody.match(/"code":".*?"/)[1]
        if (code) {
            if (code.indexOf(codeVal) > -1) {
                $.log("此code已存在，本次跳过")
            } else if (code.indexOf(codeVal) == -1) {
                codes = code + "&" + codeVal;
                $.setdata(codes, 'jd_city_withdraw_code');
                $.log(`${$.name}获取提现code: 成功, YouthBodys: ${codeVal}`);
                bodys = YouthBodys.split("&")
                $.msg($.name, "获取第" + bodys.length + "个提现code: 成功🎉", ``)
            }
        } else {
            $.setdata(codeVal, 'jd_city_withdraw_code');
            $.log(`${$.name}获取提现code: 成功, YouthBodys: ${codeVal}`);
            $.msg($.name, `获取第一个提现code: 成功🎉`, ``)
    }
}