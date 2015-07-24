#coding:UTF-8
buildbot_basedir = "/root/buildbot/master"
# configs.data item 里面包含了两个 参数 schedulers_name schedulers_force_name 必填 且不能重复
slaves=[
    {
        "dir_name":"/root/slave/dmc",
        "host":'localhost',
        "name":"slave_dmc",
        "password":"pass",
    },
    {
        "dir_name":"/root/slave/server",
        "host":'localhost',
        "name":"slave_2",
        "password":"pass",
    },
    {
        "dir_name":"/root/slave/buildbot",
        "host":'localhost',
        "name":"slave_1",
        "password":"pass",
    },
########################################################################

    {
        "dir_name":"/root/slave/prctureCompare",
        "host":'localhost',
        "name":"slave_prctureCompare",
        "password":"pass",
    },

    {
        "dir_name":"/root/slave/searchSuggest",
        "host":'localhost',
        "name":"slave_searchSuggest",
        "password":"pass",
    },

]

# data item project 必须与 slaves item name 对应（一对一）
data=[

    {
        "git":"git@github.com:yoozi/dmc.git",
        "branch":"develop",
        "workdir":"/root/storage/dmc",
        "pollinterval":60,
        "project":"slave_dmc",
        "schedulers_name":"slave_dmc_sc",
        "schedulers_force_name":"slave_dmc_scf",
        "command":[["python", buildbot_basedir+"/init_project.py"]],
    },
    {
        "git":'git@github.com:Callwoola/start-Server.git',
        "branch":"master",
        "workdir":"/root/storage/server",
        "pollinterval":1,
        "project":"slave_2",
        "schedulers_name":"all2",
        "schedulers_force_name":"force2",
        "command":[["echo", "done"],
                   ],
    },
    {
        "git":'https://github.com/Callwoola/quick-buildbot.git',
        "branch":"master",
        "workdir":"/root/storage/buildbot",
        "pollinterval":1,
        "project":"slave_1",
        "schedulers_name":"all",
        "schedulers_force_name":"force",
        "command":[["echo", "done"],
                   ],
    },
#################################################################################

    {
        "git":'https://github.com/Callwoola/pictureCompare.git',
        "branch":"master",
        "workdir":"/root/storage/pictureCompare",
        "pollinterval":1,
        "project":"slave_prctureCompare",
        "schedulers_name":"all_slave_prctureCompare",
        "schedulers_force_name":"force_slave_prctureCompare",
        "command":[["echo", "done"],
                   ],
    },

    {
        "git":'https://github.com/Callwoola/searchSuggest.git',
        "branch":"master",
        "workdir":"/root/storage/searchSuggest",
        "pollinterval":1,
        "project":"slave_searchSuggest",
        "schedulers_name":"all_slave_searchSuggest",
        "schedulers_force_name":"force_slave_searchSuggest",
        "command":[["echo", "done"],
                   ["python", buildbot_basedir+"/init_project.py"]
                   ],
    },
]

