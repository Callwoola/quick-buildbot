#!/usr/bin/env python
#coding:UTF-8
import os
import re
import sys
import subprocess

def printf(f,*l):
    print "buildbot:" + f % l

def run(*l):
    if isinstance(l[0], list):
        l = l[0]
    printf("running %s", " ".join(l))
    try:
        subprocess.check_call(l)
    except:
        pass


# Buildbot version: 0.8.12
# Twisted version: 15.1.0
# pip 自动安装 Twisted 等依赖包


# 本脚本可实现 slave 的单个配置
# 与master 设置保持一直
slaves=[
    {
        "dir_name":"slavedir2",
        "host":'localhost',
        "name":"slave_2",
        "password":"pass",
    },
    {
        "dir_name":"slavedir1",
        "host":'localhost',
        "name":"slave_1",
        "password":"pass",
    },
]


def main():
    run('pip','install','buildbot')
    run('pip','install','buildbot-slave')
    for i in slaves:
        run("buildslave","create-slave",
            i['dir_name'],
            i['host']+':'+'9989',
            i['name'],
            i['password'])

if __name__ == "__main__":
    main()

