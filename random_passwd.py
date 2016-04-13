#!/usr/bin/env python
# -*-coding:utf-8-*-

import string
import random

def random_passwd(passwd_lenth,pwd_count):
    # string.letters+string 相当于 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    # string.punctuation 相当于 '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    # string.digits 相当于 '0123456789'
    pwd_dic_str = string.letters+string.punctuation+string.digits
    for c in range(int(pwd_count)):
        pwd_list = []
        for i in range(int(passwd_lenth)):
            # choice方法是在字符串中随机取一个字符
            p = random.choice(pwd_dic_str)
            pwd_list.append(p)
            # 把列表里的字符串通过join方法拼接
            pwd_str = ''.join(pwd_list)
        print pwd_str


# 手动执行函数查看效果
random_passwd(8, 4)
