def compare_scripts():
    # 读取所有脚本文件
    scripts = [files for files in os.listdir(scriptsDir)]
    # 分类js脚本和py脚本
    jsFile = []
    pyFile = []
    tsFile = []
    for files in scripts:
        if files.find(".js", -3) != -1:
            jsFile.append(files)
        elif files.find(".py", -3) != -1:
            pyFile.append(files)
        elif files.find(".ts", -3) != -1:
            tsFile.append(files)
    # 获取脚本的文件名部分
    jsFileName = []
    i = 0
    while i < len(jsFile):
        jsFileName.append(jsFile[i].replace(".js", ""))
        i += 1
    pyFileName = []
    i = 0
    while i < len(pyFile):
        pyFileName.append(pyFile[i].replace(".py", ""))
        i += 1
    tsFileName = []
    i = 0
    while i < len(tsFile):
        tsFileName.append(tsFile[i].replace(".ts", ""))
        i += 1

    # 例外的脚本名
    exclude = ['sendNotify', 'jdCookie', 'JD_extra_cookie', 'JS_USER_AGENTS', 'USER_AGENTS', 'getJDCookie', 'index', 'tencentscf',
               'jdPlantBeanShareCodes', 'jdDreamFactoryShareCodes', 'jdJxncShareCodes', 'jdFactoryShareCodes', 'jdFruitShareCodes', 'jdPetShareCodes']
    exclude.extend(passName)
    # 对比脚本名是否存在于crontab.list中
    FileName = []  # 先将js,py和ts脚本名合并在一起
    FileName.extend(jsFileName)
    FileName.extend(pyFileName)
    FileName.extend(tsFileName)

    cronList = open(configDir + "crontab.list", "r").read()
    i = 0
    missName = ""
    while i < len(FileName):
        if cronList.find(FileName[i]) != -1:
            i += 1
        elif str(exclude).find(FileName[i]) != -1:
            i += 1
        elif cronList.find(FileName[i].replace("jd_", "")) != -1:
            i += 1
        elif str(exclude).find(FileName[i].replace("jd_", "")) != -1:
            i += 1
        else:
            missName = missName + " " + FileName[i]
            i += 1
    if missName == "":
        print('\033[32m[Done]\033[0m 比对完成，定时列表完整！🔔')
    else:
        print('\033[33m[WARN]\033[0m 定时中缺少：' + missName)


if __name__ == '__main__':
    import os
    import distro
# 定义目录路径
    if str(distro.linux_distribution()).find("Deepin") != -1:  # Deepin
        scriptsDir = "/home/wang/Documents/jd_py/jd/scripts/"
        configDir = "/home/wang/Documents/jd_py/jd/config/"
        passName = ['main.a0974cf7', 'jd_cfd_withdraw', 'jd_cfd_stock', 'jd_cfd_loop', 'jd_car_exchange', 'jd_cfd_hb',
                    'jd_speed_redEnvelope', 'jd_IndustryLottery']
    else:  # Other Linux
        scriptsDir = "/jd/scripts/"
        configDir = "/jd/config/"
        if "passName" in os.environ:
            passName = os.environ["passName"].lstrip("[").rstrip("]").split(",")
        else:
            passName = []
# 要执行的任务
    compare_scripts()
