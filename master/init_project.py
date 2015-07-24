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


# storage="/root/storage"
# copy file  to right  place

# print os.getcwd()
buildbot_path="/root/buildbot/master"
run("apt-get","-y","install","dos2unix")


# print ">>>>>>>>>>>>>>>>>>>>>> start env"
# run("dos2unix",buildbot_path+"/shell/install_php_env.sh")
# run("sudo","bash",buildbot_path+"/shell/install_php_env.sh")


print ">>>>>>>>>>>>>>>>>>>>>> start copy"
run("dos2unix",buildbot_path+"/shell/copy_file.sh")
run("sudo","bash",buildbot_path+"/shell/copy_file.sh")


composer_file_path="/root/slave/dmc/_root_storage_dmc/build/engine/composer.json"

with open(composer_file_path, 'rb+') as filehandle:
    filehandle.seek(-1, os.SEEK_END)
    filehandle.truncate()


the_repositories="""  "repositories": [
   {
     "type": "composer",
     "url": "http://192.168.1.108"
   },
   {
     "packagist": false
   }
 ],}"""

#add file
with open(composer_file_path, "a") as myfile:
    myfile.write(the_repositories)

# run("sudo","cp","-rf",storage+"/")