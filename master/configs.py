#coding:UTF-8
buildbot_basedir = '/home/neo/buildbot-develop/buildbot/master'
# configs.data item 里面包含了两个 参数 schedulers_name schedulers_force_name 必填 且不能重复
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

# data item project 必须与 slaves item name 对应（一对一）
data=[
    {
        "git":'ssh://git@git:7999/*/*-test.git',
        "branch":"develop",
        "workdir":"runtests2",
        "pollinterval":1,
        "project":"slave_2",
        "schedulers_name":"all2",
        "schedulers_force_name":"force2",
        "command":[["python", "test.py"],
                   ["python", "test.py"],
                   ["python", "test.py"],
                   ],
    },
    {
        "git":'ssh://git@git:7999/*/*-demo.git',
        "branch":"master",
        "workdir":"runtests",
        "pollinterval":1,
        "project":"slave_1",
        "schedulers_name":"all",
        "schedulers_force_name":"force",
        "command":[["python", "test.py"],
                   ["python", "test.py"],
                   ["python", "test.py"],
                   ],
    },

]

