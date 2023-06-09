# -*- coding: utf-8 -*-
"""
@Time ： 2020/8/19 下午12:06
@Auth ： apecode.
@File ： main.py
@Software  ： PyCharm
@Blog ： https://liuyangxiong.cn
"""

import json
import os
import time
import util
from yiban import Yiban
import config
from notice import Notice

# ============================================================
# Github actions 使用，本地使用请注释
try:
    config.account[0]["mobile"] = os.environ["YB_MOBILE"]
    config.account[0]["password"] = os.environ["YB_PASSWORD"]
    config.account[0]["mail"] = os.environ["YB_MAIL"]
    config.account[0]["pushToken"] = os.environ["YB_PUSHTOKEN"]
    config.account[0]["notice"] = os.environ["YB_NOTICE"]
except KeyError:
    pass
# # ===========================================================

for ac in config.account:
    yb = Yiban(ac.get("mobile"), ac.get("password"))
    nowPeriod = util.getTimePeriod()  # 获取签到时段数值
    if nowPeriod != 0:
        login = yb.login()
        if (login["response"]) != 100:
            print(login["message"])
        else:
            notice = Notice(config.admin, ac)
            auth = yb.auth()
            if auth["code"] == 0:
                # 位置签到
                yb.photoRequirements()
                yb.deviceState()
                yb.signPostion()
                ns_result = yb.nightAttendance(config.address)
                if ns_result["code"] == 0:
                    result = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))) +" 位置: " + json.loads(config.address)["Address"] + "\n"
                    notice.send(result)
                else:
                    result = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(time.time())) + "签到失败，请检查\n")
                    notice.send(result)
            else:
                print("登录授权失败，请重新登录!")
                notice.send(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(time.time())) + "登录授权失败，请重新登录\n"))
    else:
        print("未到签到时间")
