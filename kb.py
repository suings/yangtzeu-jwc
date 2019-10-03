#!/usr/bin/env python
# -*- coding=utf-8 -*-

import hashlib
import re
import time
import sys

import requests

BASE_url = "http://jwc3.yangtzeu.edu.cn/"

def pwd_sha1(page_login, pwd):
    """
    :param page_login: 登录页源码
    :param pwd:原始密码
    :return: 加密后的密码
    """
    randsrt = re.search(r"CryptoJS\.SHA1\('([a-zA-Z0-9-]+)'", page_login).group(1)
    sha = hashlib.sha1((randsrt + str(pwd)).encode('utf-8'))
    encrypts = sha.hexdigest()
    return encrypts


def login(user, pwd, sleep_time=0):
    '''

    :param user: 学号
    :param pwd: 密码
    :param sleep_time:出现过快点击时的停留时间
    :return: info: obj
    '''
    user = str(user)
    pwd = str(pwd)

    s = requests.session()
    r = s.get(BASE_url + "/eams/login.action")
    payload = {
        "username": user,
        "password": pwd_sha1(r.text, pwd),
        "encodedPassword": "",
        "session_locale": "zh_CN"
    }
    time.sleep(sleep_time)  # 防止过快点击
    r = s.post(BASE_url + "/eams/login.action", data=payload)

    info = {
        "学号": user,
        "密码": pwd,
    }
    if "请不要过快点击" in r.text:
        sleep_time += 0.5
        return login(user, pwd, sleep_time)
    if "密码错误" in r.text:
        info["状态"] = "密码错误"
        return [info, s]
    elif "账户不存在" in r.text:
        info["状态"] = "账户不存在"
        return [info, s]
    else:
        info["状态"] = "正常"
        return [info, s]


def getkb(user, pwd):
    '''

    :param user:学号
    :param pwd:密码
    :return: {data:[[教室,课程名称,第几天,第几节,""第几周有课],...],status:""}
    '''
    info, s = login(user, pwd)

    status = {
        "status": info['状态'],
    }
    if info["状态"] != "正常":
        print(info['状态'])
        return status
    else:
        # print("登录成功")
        pass

    headers = {
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    }
    page = s.get(BASE_url + "/eams/courseTableForStd.action?_=" + str(int(time.time() * 1000)), headers=headers)

    # 提取ids
    ids = re.search('bg.form.addInput\(form,"ids","(\d+)"\);', page.text).group(1)

    payload = {
        "ignoreHead": 1,
        "setting.kind": "std",
        "startWeek": "",
        "semester.id": 89,  # 为学期标志,每学期不变
        "ids": ids
    }

    page2 = s.post(BASE_url + "/eams/courseTableForStd!courseTable.action", data=payload, headers=headers)
    kb_text = page2.text
    kbs = re.findall('"([^"]+)","[^"]+","([^"]+)","(\d{53})"[^\n]+\n\t\t\tindex =(\d)\*unitCount\+(\d)', kb_text)

    value_for_return = []
    for kb in kbs:
        k_classname = kb[0][:-8]
        k_classroom = kb[1]
        k_week = kb[2]
        day = int(kb[3]) + 1
        jie = int(kb[4]) + 1
        value_for_return.append([k_classroom, k_classname, day, jie, k_week])
    status["info"] = "周是从第0周开始的"
    status['data'] = value_for_return
    cookies = requests.utils.dict_from_cookiejar(s.cookies)
    status['cookies'] = cookies
    return status


if __name__ == '__main__':
    import json

    user = ""
    pwd  = ""
    data = getkb(user,pwd)
    print(json.dumps(data, ensure_ascii=False, indent="\t"))