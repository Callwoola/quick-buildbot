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
## init build
def install():
    run('pip','install','buildbot')
    run('pip','install','buildbot-slave')
    
def start():
    run('buildbot','start','master')
def restart():
    # better than reconfig
    run('buildbot','restart','master')


def stop():
    # better than reconfig
    run('buildbot','stop','master')

def install_slave():
    import master.configs as bc
    # 根据 configs 自动安装 slave
    '''
    def find_projectname(name):
        for i in bc.data:
            if i['name'] == name:
                return i['project']
        return "empty-name"
    '''
    # 一个slave 只能对应一个 project
    for i in bc.slaves:
        run("buildslave","create-slave",
            i['dir_name'],
            i['host']+':'+'9989',
            i['name'],
            i['password'])
    # example command:
    #run("buildslave","create-slave","slave","localhost:9989","example-slave","passs")
    #print bc.slaves
def start_slave():
    import master.configs as bc
    for i in bc.slaves:
        if i['dir_name'].startswith("./"):
            if os.path.isdir(i['dir_name']):
                print "slave dir name config error:%s" % [i['dir_name']]
                exit()
        # elif i['dir_name'] not in os.listdir(os.getcwd()):
        #     print "dir not in path error:%s" % [i['dir_name']]
        #     exit()
    for i in bc.slaves:
        run("buildslave","start",
            i['dir_name'])
    # example command:
    # buildslave start slave

def stop_slave():
    import master.configs as bc
    for i in bc.slaves:
        run("buildslave","stop",
            i['dir_name'])
    # example command:
    # buildslave stop slave


def print_help():
    print "help :\n\n--------------------------------\n"
    print "start  \t buildbot "
    print "restart  \t restart buildbot"
    print "install  \t install buildbot "
    print "stop  \t\t stop buildbot"

    print "install-slave \t auto install  slave"
    print "start-slave  \t start all slave "
    print "stop-slave  \t stop slave "

#并启动
def main():
    param=str(sys.argv[1])

    if param.startswith("--help"):
        print_help()
        return
    if param == "start":
        start()
        return
    if param == "stop":
        stop()
        return
    if param == "restart":
        restart()
        return
    if param == "install":
        install()
        return
    ######### slave command split
    if param == "install-slave":
        install_slave()
        return
    if param == "start-slave":
        start_slave()
        return
    if param == "stop-slave":
        stop_slave()
        return
    print_help()



if __name__ == "__main__":
    main()

